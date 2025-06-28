import json
import sys
from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
import pathlib
import re

from tariff_engine.constants import DUES_TYPES
from tariff_engine.prompts import EXTRACT_RULES_PROMPT, CALCULATE_SPECIFIC_DUES_PROMPT

LLM_MODEL = "gemini-2.5-pro"

load_dotenv()

class PortDuesChatbot:
    def __init__(self):
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("❌ GEMINI_API_KEY not found in environment variables. Please check your .env file.")
        self.client = genai.Client(api_key=api_key)
        self.vessel_data = None
        self.rules_extracted = False
        self.rules_path = "rubrics.md"
        self.debug_mode = False
        
    def extract_response_content(self, response, clean_output=True):
        """
        Extract content from Gemini response, optionally cleaning up code execution details
        """
        full_content = []
        
        try:
            for candidate in response.candidates:
                for part in candidate.content.parts:
                    if hasattr(part, 'text') and part.text:
                        full_content.append(part.text)
                    elif not clean_output:  # Only include code details in debug mode
                        if hasattr(part, 'executable_code') and part.executable_code:
                            if hasattr(part.executable_code, 'code') and part.executable_code.code:
                                full_content.append(f"\n```python\n{part.executable_code.code}\n```")
                        elif hasattr(part, 'code_execution_result') and part.code_execution_result:
                            if hasattr(part.code_execution_result, 'output') and part.code_execution_result.output:
                                full_content.append(f"\n**Execution Result:**\n{part.code_execution_result.output}")
            
            content = '\n'.join(full_content) if full_content else ""
            original_content = content  # Keep original for fallback
            
            if clean_output:
                content = self.clean_response_content(content)
            
            # Simple fix: if cleaning resulted in empty/None, return a retry signal
            if not content or content.strip().lower() in ["none", "", "null"]:
                return "RETRY_NEEDED"
            
            return content
        except Exception as e:
            # Fallback to simple text extraction
            fallback = getattr(response, 'text', str(response))
            return f"❌ Error processing response: {str(e)}\n\nRaw response: {fallback}"

    def clean_response_content(self, content):
        """
        Extract only the final results, removing all explanations and calculations
        """
        # Quick check for already formatted results - if found, return as-is
        import re
        if re.search(r'•\s*\*\*[^:]+:\*\*\s*[A-Z]{1,3}\s*[\d,]+', content):
            return content
        
        # Remove Python code blocks
        content = re.sub(r'```python\n.*?\n```', '', content, flags=re.DOTALL)
        
        # Remove execution result sections
        content = re.sub(r'\*\*Execution Result:\*\*\n.*?(?=\n\n|\n[A-Z#]|\Z)', '', content, flags=re.DOTALL)
        
        # Remove explanatory text
        content = re.sub(r'(Answering your|My thinking process|Here are the detailed calculations).*?(?=###|##|$)', '', content, flags=re.DOTALL)
        
        # Keep only Final Results section
        final_results_match = re.search(r'(###?\s*Final Results?:.*?)(?=\n###|\n##|$)', content, flags=re.DOTALL)
        if final_results_match:
            content = final_results_match.group(1)
        else:
            # Look for cost amounts in the format "**Name:** Amount"
            cost_matches = re.findall(r'\*\*([^:]*(?:Dues?|Cost)[^:]*?):\*\*\s*[^\n]*?([A-Z]{1,3}\s*[\d,]+\.?\d*)', content)
            if cost_matches:
                results = ""
                for due_name, amount in cost_matches:
                    results += f"• **{due_name.strip()}:** {amount}\n"
                content = results
        
        # Clean up multiple newlines
        content = re.sub(r'\n{3,}', '\n\n', content)
        
        return content.strip()

    def extract_rules_for_dues(self, specific_dues=None):
        """
        Extract rules for specific dues or all dues
        """
        try:
            filepath = pathlib.Path('Port Tariff.pdf')
            if not filepath.exists():
                return False, "❌ Port Tariff.pdf not found. Please ensure the file is in the current directory."
            
            dues_to_extract = specific_dues if specific_dues else DUES_TYPES
            rules_list = "\n".join([f'- {due}' for due in dues_to_extract])
            
            prompt = EXTRACT_RULES_PROMPT.format(rules_list=rules_list)
            
            print("🤖 Extracting rules from PDF...")
            response = self.client.models.generate_content(
            model=LLM_MODEL,
            contents=[
                types.Part.from_bytes(
                    data=filepath.read_bytes(),
                    mime_type='application/pdf',
                ),
                prompt,
            ],
                config=types.GenerateContentConfig(
                    safety_settings=[
                        types.SafetySetting(
                            category='HARM_CATEGORY_HATE_SPEECH',
                            threshold='BLOCK_ONLY_HIGH'
                        ),
                        types.SafetySetting(
                            category='HARM_CATEGORY_HARASSMENT',
                            threshold='BLOCK_ONLY_HIGH'
                        ),
                        types.SafetySetting(
                            category='HARM_CATEGORY_SEXUALLY_EXPLICIT',
                            threshold='BLOCK_ONLY_HIGH'
                        ),
                        types.SafetySetting(
                            category='HARM_CATEGORY_DANGEROUS_CONTENT',
                            threshold='BLOCK_ONLY_HIGH'
                        ),
                    ],
                )
            )

            rules_content = self.extract_response_content(response, clean_output=False)
            
            with open(self.rules_path, "w", encoding="utf-8") as f:
                f.write(rules_content)
            
            self.rules_extracted = True
            return True, "✅ Rules extracted successfully!"

        except Exception as e:
            return False, f"❌ Error extracting rules: {str(e)}"

    def calculate_specific_dues(self, requested_dues, _is_fallback=False):
        """
        Calculate specific dues based on vessel data
        """
        if not self.vessel_data:
            return "❌ Please provide vessel data first using the 'input' command."
        
        if not self.rules_extracted:
            if pathlib.Path(self.rules_path).exists():
                print("✅ Using existing rules file (rubrics.md)")
                self.rules_extracted = True
            else:
                success, message = self.extract_rules_for_dues()
                if not success:
                    return message
        
        try:
            with open(self.rules_path, 'r', encoding='utf-8') as f:
                rules = f.read()

            dues_list = ", ".join(requested_dues)
            
            prompt = CALCULATE_SPECIFIC_DUES_PROMPT.format(
                rules=rules,
                vessel_data=self.vessel_data,
                dues_list=dues_list
            )
            
            print("🤖 Calculating requested dues...")
            response = self.client.models.generate_content(
            model=LLM_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[types.Tool(code_execution=types.ToolCodeExecution())],
                    temperature=0.1,
                    safety_settings=[
                        types.SafetySetting(
                            category='HARM_CATEGORY_HATE_SPEECH',
                            threshold='BLOCK_ONLY_HIGH'
                        ),
                        types.SafetySetting(
                            category='HARM_CATEGORY_HARASSMENT',
                            threshold='BLOCK_ONLY_HIGH'
                        ),
                        types.SafetySetting(
                            category='HARM_CATEGORY_SEXUALLY_EXPLICIT',
                            threshold='BLOCK_ONLY_HIGH'
                        ),
                        types.SafetySetting(
                            category='HARM_CATEGORY_DANGEROUS_CONTENT',
                            threshold='BLOCK_ONLY_HIGH'
                        ),
                    ],
                )
            )
            
            # Use clean output unless in debug mode
            result = self.extract_response_content(response, clean_output=not self.debug_mode)
            
            # If individual calculation failed, try fallback to "calculate all" and extract requested dues
            if result == "RETRY_NEEDED" and len(requested_dues) == 1 and not _is_fallback:
                try:
                    # Silently try calculating all dues and extract the one we need
                    all_result = self.calculate_specific_dues(DUES_TYPES, _is_fallback=True)
                    if all_result and all_result != "RETRY_NEEDED":
                        # Extract just the requested due from the "all" result
                        import re
                        requested_due = requested_dues[0]
                        pattern = f"• \\*\\*{re.escape(requested_due)}:\\*\\* ([^\\n]+)"
                        match = re.search(pattern, all_result)
                        if match:
                            return f"• **{requested_due}:** {match.group(1)}"
                except:
                    pass  # If fallback fails, continue with original result
            
            return result if result != "RETRY_NEEDED" else f"• **{requested_dues[0]}:** Unable to calculate at this time. Please try 'calculate all'."

        except Exception as e:
            return f"❌ Error calculating dues: {str(e)}"

    def set_vessel_data(self, data):
        """
        Input for calculations
        """
        self.vessel_data = data
        return "✅ Vessel data saved! You can now ask me to calculate specific dues."

    def get_available_dues(self):
        """
        Return list of available dues
        """
        return "📋 Available dues I can calculate:\n" + "\n".join([f"• {due}" for due in DUES_TYPES])
    
    def chat(self):
        """
        Main chatbot interface
        """
        print("="*60)
        print("🚢 Port Dues Calculator Chatbot")
        print("="*60)
        print("👋 Hello! I can help you calculate port dues for vessels.")
        print("🛡️  Safety settings enabled for responsible AI usage")
        print("\n📝 Available commands:")
        print("• 'input' - Input your vessel information")
        print("• 'calculate [due names]' - Calculate specific dues")
        print("• 'calculate all' - Calculate all available dues")
        print("• 'available dues' - Show all available due types")
        print("• 'debug on/off' - Enable/disable debug mode")
        print("• 'help' - Show this help message")
        print("• 'quit' - Exit the chatbot")
        print("\n" + "="*60)
        
        while True:
            try:
                user_input = input("\n💬 You: ").strip().lower()
                
                if user_input in ['quit', 'exit', 'bye']:
                    print("👋 Goodbye! Have a great day!")
                    break
                
                elif user_input == 'help':
                    print("\n📝 Available commands:")
                    print("• 'input' - Input your vessel information")
                    print("• 'calculate [due names]' - Calculate specific dues (e.g., 'calculate port dues, pilotage dues')")
                    print("• 'calculate all' - Calculate all available dues")
                    print("• 'available dues' - Show all available due types")
                    print("• 'debug on/off' - Enable/disable debug mode")
                    print("• 'help' - Show this help message")
                    print("• 'quit' - Exit the chatbot")
                
                elif user_input == 'debug on':
                    self.debug_mode = True
                    print("\n🤖 Bot: ✅ Debug mode enabled - Will show detailed calculations")
                
                elif user_input == 'debug off':
                    self.debug_mode = False
                    print("\n🤖 Bot: ✅ Debug mode disabled - Will show clean results only")
                
                elif user_input == 'available dues':
                    print(f"\n🤖 Bot: {self.get_available_dues()}")
                
                elif user_input == 'input':
                    print("\n📋 Please paste your vessel data below.")
                    print("When finished, press Ctrl+Z (Windows) or Ctrl+D (Mac/Linux) and then Enter:")
                    print("-" * 50)
                    try:
                        vessel_data = sys.stdin.read().strip()
                        if vessel_data:
                            response = self.set_vessel_data(vessel_data)
                            print(f"\n🤖 Bot: {response}")
                        else:
                            print("\n🤖 Bot: ❌ No vessel data received. Please try again.")
                    except KeyboardInterrupt:
                        print("\n❌ Data input cancelled.")
                    except EOFError:
                        print("\n❌ Data input cancelled.")
                
                elif user_input.startswith('calculate'):
                    if user_input == 'calculate all':
                        requested_dues = DUES_TYPES
                    else:
                        # Extract specific dues from user input
                        dues_text = user_input.replace('calculate', '').strip()
                        if not dues_text:
                            print("\n🤖 Bot: ❌ Please specify which dues to calculate or use 'calculate all'")
                            continue
                        
                        # Improved matching logic for specific dues
                        requested_dues = []
                        dues_input = dues_text.lower()
                        
                        if self.debug_mode:
                            print(f"\n🔍 Debug: Processing '{dues_text}' -> '{dues_input}'")
                        
                        # Add VTS expansion for better matching
                        input_keywords = dues_input.replace(" dues", "").split()
                        if ('vessel' in input_keywords and 'traffic' in input_keywords) or \
                           ('vehicle' in input_keywords and 'traffic' in input_keywords):
                            dues_input += " vts"
                            if self.debug_mode:
                                print(f"🔍 Debug: VTS expansion applied -> '{dues_input}'")
                        
                        # Check for exact or partial matches
                        for due in DUES_TYPES:
                            due_lower = due.lower()
                            # Remove "dues" from both for better matching
                            due_keywords = due_lower.replace(" dues", "").split()
                            input_keywords = dues_input.replace(" dues", "").split()
                            
                            if self.debug_mode:
                                print(f"🔍 Debug: Checking '{due}' -> {due_keywords} vs {input_keywords}")
                            
                            # Check if any significant keyword matches
                            for input_word in input_keywords:
                                if len(input_word) > 2:  # Ignore short words like "of"
                                    if any(input_word in due_word or due_word in input_word 
                                          for due_word in due_keywords):
                                        if due not in requested_dues:
                                            requested_dues.append(due)
                                            if self.debug_mode:
                                                print(f"🔍 Debug: ✅ MATCHED '{due}' with '{input_word}'")
                                        break
                        
                        if not requested_dues:
                            print(f"\n🤖 Bot: ❌ No matching dues found for '{dues_text}'. {self.get_available_dues()}")
                            continue
                    
                    print(f"\n🤖 Bot: Calculating: {', '.join(requested_dues)}")
                    result = self.calculate_specific_dues(requested_dues)
                    print(f"\n🤖 Bot:\n{result}")
                
                else:
                    print("\n🤖 Bot: ❓ I didn't understand that command. Type 'help' to see available commands.")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye! Have a great day!")
                break
            except EOFError:
                print("\n\n👋 Goodbye! Have a great day!")
                break 