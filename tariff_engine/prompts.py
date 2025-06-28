"""
Prompts used by the Port Dues Chatbot
"""

EXTRACT_RULES_PROMPT = """Extract all relevant rules and formulas for calculating the following dues from the attached PDF:
{rules_list}

For each due type, provide all relevant tables, rates, and conditions. Structure the output clearly with a heading for each due type.

Example Output Format:
# Port Dues
## General Rules and Guidelines:
...
## Data Tables:
...
## Formulas:
...

IMPORTANT:
Ensure you correctly parse monetary values, for example:
"Mooring ropes at the Port of Saldanha…………………………….…………………………………..1 511.85 " - Cost should be taken as 1511.85 not 511.85
"""

CALCULATE_SPECIFIC_DUES_PROMPT = """Based on the following rules and guidelines extracted from the tariff document:
<rules>
{rules}
</rules>

And the following vessel and port information:
<input>
{vessel_data}
</input>

Calculate ONLY the final cost amounts for: {dues_list}

CRITICAL REQUIREMENTS:
1. For Port Dues, ALWAYS use "Days Alongside" if explicitly mentioned
2. Use code execution for mathematical calculations to ensure accuracy
3. NO explanations, NO step-by-step calculations, NO thinking process
4. ONLY provide the final monetary amounts

Format your response EXACTLY as:
• **Port Dues:** ZAR X,XXX.XX
• **Light Dues:** ZAR X,XXX.XX
(etc. for each requested due)

Do NOT include any calculations, explanations, formulas, or reasoning. Just the final amounts.
""" 