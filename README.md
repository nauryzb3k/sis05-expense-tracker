# Expense Tracker

A simple command-line application for recording and tracking expenses.

## Features
- Add expenses with an amount, category, and description.
- Display all recorded expenses.
- Calculate total expenses.
- Filter expenses by category.

## Acceptance Criteria
1. The application accepts valid expenses with positive amounts.
2. The application rejects zero or negative amounts.
3. The application rejects empty categories.
4. The application calculates total expenses correctly.
5. The application filters expenses by category without case sensitivity.

## Project Structure
- `expense_tracker.py` — application logic and command-line interface.
- `test_expense_tracker.py` — automated unit tests.

## Requirements
- Python 3.10 or newer.
- No external dependencies.

## Run
`python expense_tracker.py`

## Test
`python -m unittest -v`
