import os
from dotenv import load_dotenv
from revChatGPT.V1 import Chatbot

load_dotenv()
access_token = os.environ.get("CHAT_GPT_ACCESS_TOKEN")

chat_config = {
    "access_token": access_token,
    "model": "gpt-4",
    "disable_history": True,
}
chatbot = Chatbot(config=chat_config)


def main() -> None:
    print("Welcome to ChatGPT CLI")
    while True:
        prompt = input("> ")
        response = ""
        for data in chatbot.ask(prompt):
            response = data["message"]
        print(response)


if __name__ == "__main__":
    main()
