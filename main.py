import sys, os
import json
from google import genai
from google.genai import types
from dotenv import load_dotenv
import pathlib
import re

from tariff_engine.constants import DUES_TYPES
from tariff_engine.chatbot import PortDuesChatbot

# Load environment variables
load_dotenv()

def main():
    """
    Start the chatbot
    """
    chatbot = PortDuesChatbot()
    chatbot.chat()

if __name__ == "__main__":
    main() 