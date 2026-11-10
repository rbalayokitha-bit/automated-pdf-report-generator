# Automated PDF Report Generator

## Project Overview

Automated PDF Report Generator is a Python-based application that fetches data from an external API, processes the collected information, and generates professional PDF reports automatically.

## Features

- Fetches data using REST API.
- Processes and analyzes collected data.
- Generates PDF reports using ReportLab.
- Provides a command-line interface.
- Supports automated report scheduling.
- Includes unit testing with 100% code coverage.

## Technologies Used

- Python
- FastAPI-compatible REST API integration (Requests)
- ReportLab
- APScheduler
- Pytest
- Setuptools

## Project Structure

```text
Automated-PDF-Report-Generator/
│
├── app/
│   ├── __init__.py
│   ├── api.py
│   ├── processor.py
│   ├── pdf_generator.py
│   ├── scheduler.py
│   └── cli.py
│
├── reports/
├── tests/
├── main.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Install dependencies:

```bash
pip install -e ".[dev]"
```

## Usage

Run the complete application:

```bash
python main.py
```

Generate a report using CLI:

```bash
report-generator --limit 5
```

Start automated scheduling:

```bash
python app/scheduler.py
```

## Testing

Run unit tests:

```bash
python -m pytest -v
```

Check code coverage:

```bash
python -m pytest --cov=app --cov