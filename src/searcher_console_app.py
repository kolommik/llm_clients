"""This module provides utilities to perform a Google search using the
SERPAPI library and generate answers
using OpenAI's GPT-3.5 Turbo API.
"""
import os
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from searcher import (
    get_answer_by_gpt_35_turbo,
    perform_google_search,
    create_info_prompt,
)


def main() -> None:
    # Initialize the Console
    console = Console()

    # Prompt the user for a question
    question = console.input("[bold magenta]What is your question? [/bold magenta]")

    # Perform a Google search using the SERPAPI library and generate a prompt with
    # information from the search results.
    results = perform_google_search(question)

    # Create prompt info text from searching results
    info_prompt = create_info_prompt(question, results)

    if not info_prompt:
        console.print("[bold red] No search results found.[/bold red]")
        return

    console.print(f"Prompt\n[bold green]{info_prompt}[/bold green]!")

    # Answer from OpenAI
    usage, answer = get_answer_by_gpt_35_turbo(info_prompt)

    usage_text = Text(str(usage), style="bold blue")
    usage_panel = Panel(usage_text, box=box.SQUARE, expand=False)
    console.print(usage_panel)

    console.print(f"[bold blue]Answer: {answer}[/bold blue]!")

    print("Done")
    os.system("pause")


if __name__ == "__main__":
    main()
