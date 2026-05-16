# Python CI/CD Pipeline using GitHub Actions

A fully automated CI/CD pipeline for a Python application — runs on every push to `main`.

## Pipeline Steps (automated)
```
Push to main
    ↓
Install dependencies
    ↓
Lint with flake8
    ↓
Run unit tests (4 test cases)
    ↓
Deploy to AWS (on success)
```

## Prerequisites
- GitHub repository
- AWS account (for deployment step)
- Add these GitHub Secrets:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`

## How to Use
1. Push this folder to a GitHub repo
2. Every push to `main` triggers the pipeline automatically
3. Check the **Actions** tab in GitHub to see live pipeline runs

## Project Structure
```
3-python-cicd-pipeline/
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # GitHub Actions pipeline definition
├── app/
│   ├── __init__.py
│   └── calculator.py       # Sample Python app
├── tests/
│   ├── __init__.py
│   └── test_calculator.py  # 4 unit test cases
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Running Locally
```bash
pip install -r requirements-dev.txt
flake8 app/ tests/
python -m pytest tests/ -v
```
