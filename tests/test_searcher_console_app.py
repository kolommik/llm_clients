"""test_searcher_console_app.py

This module contains unit tests for the searcher_console_app.py module.
"""
from unittest.mock import patch
from pytest import CaptureFixture
from pytest_mock import MockFixture
import searcher
from searcher_console_app import main


def test_main_no_search_results(capsys: CaptureFixture[str]) -> None:
    with patch("builtins.input", return_value="dgrdsger6esfe463464e34tte356et354t45"):
        main()
    captured = capsys.readouterr()
    assert "No search results found." in captured.out


def test_main_with_search_results(
    mocker: MockFixture, capsys: CaptureFixture[str]
) -> None:
    mocker.patch("searcher.perform_google_search")
    searcher.perform_google_search.return_value = {
        "knowledge_graph": {"description": "What is the capital of France?"}
    }
    mocker.patch("searcher.get_answer_by_gpt_35_turbo")
    searcher.get_answer_by_gpt_35_turbo.return_value = (
        {"usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}},
        "What is the capital of France?",
    )

    with patch("builtins.input", return_value="What is the capital of France?"):
        main()

    captured = capsys.readouterr()
    valid_answers = (
        "Answer: The capital of France is Paris.",
        "Answer: Paris is the capital of France.",
    )
    assert any(answer in captured.out for answer in valid_answers)
