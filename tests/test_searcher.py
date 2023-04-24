"""test_searcher.py

This module contains unit tests for the functions in the searcher.py module.
"""
from typing import Dict, Any
import pytest
from pytest_mock import MockFixture
from searcher import (
    get_answer_by_gpt_35_turbo,
    perform_google_search,
    create_info_prompt,
)


@pytest.mark.parametrize(
    "prompt, expected_answer",
    [
        ("What is the capital of France in one word?", "Paris."),
    ],
)
def test_get_answer_by_gpt_35_turbo(prompt: str, expected_answer: str) -> None:
    _, answer = get_answer_by_gpt_35_turbo(prompt)
    assert answer.strip() == expected_answer


def test_perform_google_search(mocker: MockFixture) -> None:
    mocker.patch("searcher.perform_google_search")
    perform_google_search.return_value = {"search_metadata": {}}
    question = "What is the capital of France?"
    results = perform_google_search(question)
    assert "search_metadata" in results


@pytest.mark.parametrize(
    "question, results, expected_prompt",
    [
        ("Empty Prompt", {}, ""),
        (
            "What is the square root of 16?",
            {"knowledge_graph": {"description": "4"}},
            (
                "Use the following sources to answer the MAIN QUESTION.\n\n"
                + "Info: 4\n\n\n\n"
                + "MAIN QUESTION: What is the square root of 16?\n\nAnswer:"
            ),
        ),
    ],
)
def test_create_info_prompt(
    question: str, results: Dict[Any, Any], expected_prompt: str
) -> None:
    prompt = create_info_prompt(question, results)
    print(prompt)
    assert prompt == expected_prompt
