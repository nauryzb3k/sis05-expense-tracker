# Project memory

## Product intent & audience

- Simple Python CLI expense tracker for personal use / learning
- Core features: add expense, list expenses, view total, filter by category
- Expected to have associated unit tests (`test_expense_tracker.py`)

## Brand personality & voice

- Technical, direct communication
- Caveats and constraints surfaced up front before delivering requested output

## Visual design & UX direction

- Terminal/CLI app; numbered text menu driven loop
- No graphical UI; output formatted as `f'{category}: {amount:.2f} - {description}'`
- Currency values rounded to 2 decimal places in display and storage

## Decisions, constraints & rationale

- **Not a git repository**: project has no git repo or GitHub connection; "GitHub baseline" diffs are not possible. User has been informed.
- **Read-only constraint**: user explicitly forbids modifying, committing, or pushing project files for diff requests.
- **Architecture**: refactored from module-level global `expenses` list to `ExpenseManager` class with instance state (`self._expenses`).
- **Validation rules**: amount must be > 0 (rejects zero and negative); category must be non-empty after strip.
- **Data shape**: expense is a dict with keys `amount` (float, rounded 2dp), `category` (stripped), `description` (stripped, defaults to "").
- **Encapsulation**: `get_expenses()` returns a shallow copy via `list()` to prevent external mutation of internal state.
- **Category filtering**: case-insensitive comparison.
- **Test isolation**: each test uses a fresh `ExpenseManager()` in `setUp`; no shared global state. Tests cover instance independence and returned-list immutability.
- **Test framework**: `unittest`.

## Open questions & assumptions

- User references "GitHub baseline" despite no git repo — unclear if they plan to initialize git.
- Unknown whether persistent storage (file/database) is planned; current data is in-memory only.
- No `.bolt/prompt` file exists; all global instructions are absent — inferred context only.