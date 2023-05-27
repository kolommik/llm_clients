"""This module implements a chat application using the ChatBard API from bardapi.

It loads environment variables using dotenv, then creates an instance of
ChatBard and starts a chat session.

Usage:
    python main.py

Environment Variables:
    To properly use this application, the appropriate environment variables
    should be set in a .env file.
"""
from dotenv import load_dotenv
from bardapi.chat import ChatBard

# Load environment variables from .env file.
load_dotenv()

if __name__ == "__main__":
    # Instantiate ChatBard and start the chat session.
    chat = ChatBard()  # type: ignore
    chat.start()  # type: ignore
