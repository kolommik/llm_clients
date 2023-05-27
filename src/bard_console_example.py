"""This module interacts with the Bard API to run a chat session in Russian language.

It retrieves an API key from environment variables, using python-dotenv to load them
from a .env file, then uses that key to instantiate a Bard object.

Usage:
    python main.py

Environment Variables:
    To properly use this application, the '_BARD_API_KEY' environment variable should
    be set in a .env file.
"""
import os
from dotenv import load_dotenv
from bardapi.core import Bard

# Load environment variables from .env file.
load_dotenv()
bard_cookie = os.environ.get("_BARD_API_KEY", "")


if __name__ == "__main__":
    if bard_cookie is None:
        raise ValueError("Missing environment variable: _BARD_API_KEY")

    # Instantiate Bard and start a chat session in Russian.
    # It uses internal translator
    bard = Bard(token=bard_cookie, language="russian")
    print(bard.get_answer("Как тебя зовут?")["content"])

    print("Done")
    os.system("pause")
