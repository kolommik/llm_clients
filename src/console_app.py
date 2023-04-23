"""This module provides utilities to perform a Google search using the
SERPAPI library and generate answers
using OpenAI's GPT-3.5 Turbo API.
"""
from typing import Tuple, Dict, Any
import os
from dotenv import load_dotenv
import openai
from serpapi import GoogleSearch
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")
serpapi_api_key = os.environ.get("SERPAPI_API_KEY")


def get_answer_by_gpt_35_turbo(prompt: str) -> Tuple[Dict[str, Any], str]:
    """Generate an answer to a given prompt using OpenAI's GPT-3.5 Turbo API.

    Parameters
    ----------
    prompt : str
        The input prompt to be answered by GPT-3.5 Turbo.

    Returns
    -------
    Tuple[Dict[str, Any], str]
        A tuple containing the usage information and the generated answer from
        GPT-3.5 Turbo.

    Notes
    -----
    This function requires a valid OpenAI API key to work. The following settings
    are used:
    - Model: GPT-3.5 Turbo
    - Maximum tokens: 1024
    - Number of responses: 1
    - Temperature: 0.7

    Example
    -------
    >>> openai_api_key = "your_api_key_here"
    >>> prompt = "What is the capital of France?"
    >>> usage, answer = get_answer_by_gpt_35_turbo(prompt)
    """
    chat_prompt = [{"role": "user", "content": prompt}]

    # Use OpenAI's GPT-3.5 Turbo API to answer the question
    openai.api_key = openai_api_key

    response = openai.ChatCompletion.create(  # type: ignore
        model="gpt-3.5-turbo",
        messages=chat_prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # The answer from OpenAI
    answer = response["choices"][0]["message"]["content"]

    return (response["usage"], answer)


def main() -> None:
    # Initialize the Console
    console = Console()

    # ===============================
    # Prompt the user for a question
    question = console.input("[bold magenta]What is your question? [/bold magenta]")

    # ===============================
    # Perform a Google search using the SERPAPI library and generate a prompt with
    # information from the search results.
    params = {
        "api_key": serpapi_api_key,
        "engine": "google",
        "q": question,
        "location": "Austin, Texas, United States",
        "google_domain": "google.com",
        "gl": "us",
        "hl": "en",
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    # ==============================================
    # Create prompt info text from searching results
    knowledge_graph_info = (
        f'Info: {results["knowledge_graph"]["description"]}'
        if "knowledge_graph" in results and "description" in results["knowledge_graph"]
        else ""  # No knowledge graph information found
    )
    related_questions_info = [
        f'Question: {rq["question"]}\nAnswer: {rq.get("snippet","No answer found.")}'
        for rq in results.get("related_questions", [])
    ]
    search_results_info = [
        (
            f"Source:\n"
            f'Title: {sr["title"]}\n'
            f'Content: {sr.get("snippet","No answer found.")}'
        )
        for sr in results.get("organic_results", [])
    ]
    search_results_related_questons_info = [
        f'Question: {rq["question"]}\nAnswer: {rq["snippet"]}'
        for item in results.get("organic_results", [])
        if item.get("related_questions", None) is not None
        for rq in item["related_questions"]
    ]

    search_results_len = (
        len(knowledge_graph_info)
        + len(search_results_info)
        + len(related_questions_info)
        + len(search_results_related_questons_info)
    )

    # No search results found
    if search_results_len == 0:
        console.print("[bold red] No search results found.[/bold red]")
        return

    # searched results
    serch_info = (
        "\n\n".join([knowledge_graph_info])
        + "\n\n"
        + "\n\n".join(search_results_info)
        + "\n\n".join(related_questions_info)
        + "\n\n".join(search_results_related_questons_info)
    )

    info_prompt = (
        "Use the following sources to answer the MAIN QUESTION:\n\n"
        + serch_info
        + "\n\nMAIN QUESTION: "
        + question
        + "\n\nAnswer:"
    )

    console.print(f"Prompt, [bold green]{info_prompt}[/bold green]!")
    # ===============================

    # Answer from OpenAI
    usage, answer = get_answer_by_gpt_35_turbo(info_prompt)

    console.print(f"Usage, [bold yellow]{usage}[/bold yellow]!")
    print(type(usage))
    usage_text = Text(str(usage), style="bold blue")
    usage_panel = Panel(usage_text, box=box.SQUARE, expand=False)
    console.print(usage_panel)

    console.print(f"Answer, [bold blue]{answer}[/bold blue]!")

    # ===============================
    input("Press any key to end...")


if __name__ == "__main__":
    main()
