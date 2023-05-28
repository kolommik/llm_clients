# GitHub Language Model Clients

This project is a collection of command-line clients for searching and retrieving answers to user questions using various language models and search engines.

## Features

- Query Google's search engine for answers to questions
- Use OpenAI's GPT-3.5-turbo to generate answers based on the information found in search results
- Interactive command-line interface for user input
- Integrated with Bing's Chat, also known as Sydney, using the SydneyClient (https://github.com/vsakkas/sydney.py)
- Provides the ability to run chat sessions in Russian language using Google's Bard chat (https://github.com/dsdanielpark/Bard-API)

## Installation

### Requirements

- Python 3.10 or higher
- [Poetry](https://python-poetry.org/) for package management

### Setup

1. Clone the repository:

```bash
git clone https://github.com/kolommik/gh_llm_clients.git
```

2. Navigate to the project directory:

```bash
cd gh_llm_clients
```

3. Install dependencies using Poetry:

```bash
poetry install
```

4. Activate the virtual environment:

```bash
poetry shell
```

## Usage

To start the command-line client, run:

```bash
python src/searcher_console_app.py
```

Follow the prompts to enter your question and view the generated answers.

## Testing

To run the tests using 'pytest', run the following command:

```bash
poetry run pytest
```


