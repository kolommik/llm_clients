"""This script interacts with the Sydney AI model using the SydneyClient. It takes
inputs from the user and sends it to Sydney, then prints Sydney's responses.

Environment Variables:
    BING_U_COOKIE : A cookie from Bing search. It's used for the SydneyClient.

Dependencies:
    - os
    - asyncio
    - dotenv
    - sydney
"""
import os
import asyncio
from dotenv import load_dotenv
from sydney.sydney import SydneyClient

load_dotenv()
bing_u_cookie = os.environ.get("BING_U_COOKIE")


async def main() -> None:
    async with SydneyClient(
        style="balanced", bing_u_cookie=bing_u_cookie, use_proxy=False
    ) as sydney:
        while True:
            prompt = input("You: ")

            if prompt == "!reset":
                await sydney.reset_conversation()
                continue
            elif prompt == "!exit":
                break

            print("Sydney: ", end="", flush=True)
            async for response in sydney.ask_stream(prompt):
                print(response, end="", flush=True)
            print("\n")


if __name__ == "__main__":
    asyncio.run(main())
