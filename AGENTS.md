# AGENTS.md

## Project Purpose
Expense Tracker is a small Python command-line application for recording and calculating expenses.

## Architecture
- `expense_tracker.py`: application logic and CLI.
- `test_expense_tracker.py`: unit tests.
- `README.md`: project documentation.

## Environment Setup
- Python 3.10 or newer.
- No third-party dependencies are required.

## Safe Commands
- `python expense_tracker.py`
- `python -m unittest -v`
- `git status`
- `git diff`
- `git log`

## Coding Conventions
- Follow PEP 8.
- Use descriptive function and variable names.
- Keep functions small and focused.
- Validate user input.
- Add or update tests when changing behavior.

## Testing Expectations
- Run `python -m unittest -v` after code changes.
- Do not claim tests passed unless they were actually executed.
- Report any tests that could not be run.

## Security and Restrictions
- Never access, display, or expose secrets, credentials, or private user data.
- Never deploy to production.
- Never run destructive commands such as `rm -rf`.
- Never use `git push --force`.
- Do not install, remove, or update dependencies without human approval.
- Do not delete project files without human approval.
- Do not modify files outside this repository.
- Do not commit or push changes without human approval.

## Human Review
A human must review all proposed code changes, test results, and Git diffs before they are accepted.
