# SIS #05 — AI-Assisted Software Engineering Report

## 1. Project Overview

**Project:** Expense Tracker  
**Repository:** https://github.com/nauryzb3k/sis05-expense-tracker  
**Language:** Python 3.10+  
**Application type:** Command-line application  
**Dependencies:** Python standard library only.

The application records expenses, displays them, calculates totals, and filters expenses by category.

### Repository history

| Milestone | Commit |
|---|---|
| Initial baseline | `a7b4945` |
| Documentation and agent instructions | `1fa64ad` |
| ExpenseManager refactoring | `1fbefde` |
| Data protection and finite amount validation | `78e9618` |
| Repository cleanup | `ab9cf70` |
| Background-agent safety policy | `c22afec` |

The initial baseline was tagged `baseline`.

## 2. Repository Structure

Main project files:

- `expense_tracker.py` — application logic and CLI.
- `test_expense_tracker.py` — automated unit tests.
- `README.md` — project description, requirements, run instructions and acceptance criteria.
- `AGENTS.md` — instructions and restrictions for AI coding agents.
- `AGENT_SAFETY_PLAN.md` — background-agent safety policy.
- `.gitignore` — ignores Python cache files, virtual environments, Bolt files and environment files.

The repository initially contained unnecessary generated files: Python bytecode, a Bolt memory file and an npm lock file. These were removed from Git tracking. The `.gitignore` file was updated to prevent such files from being tracked again.

## 3. Baseline and Testing Evidence

The initial baseline test run completed successfully:

- Baseline: 5 tests passed.
- After the ExpenseManager refactoring: 11 tests passed.
- After the two risk mitigations: 14 tests passed.

The final test command used was:

`python -m unittest -v`

The final observed test summary was:

`Ran 14 tests in 0.002s`
`OK`

The tests cover adding expenses, category filtering, total calculation, input validation, manager isolation, defensive copies and non-finite numeric values.

No test result is claimed for checks that were not executed.

## 4. AI Risk Review

The source code was reviewed for data integrity, input validation, availability, reliability and security risks.

| ID | Category | Finding | Classification | Evidence |
|---|---|---|---|---|
| R1 | Data integrity | Returning an internal expense dictionary could allow callers to modify stored data. | Confirmed | The returned object was mutable; a regression test now verifies defensive copying. |
| R2 | Input validation | NaN and Infinity could pass a simple positive-number check. | Confirmed | The original check only compared the amount with zero; tests now verify rejection. |
| R3 | Data availability | Expenses are stored in memory and disappear when the process exits. | Confirmed | The application uses an in-memory collection without persistence. |
| R4 | Input validation | Non-string category or description values may cause an AttributeError when string methods are called. | Confirmed | The code uses string operations without comprehensive type validation. |
| R5 | Reliability | Unexpected end-of-input may raise an unhandled EOFError in the CLI. | Plausible | No explicit EOF handling was identified in the reviewed CLI flow. |
| R6 | Security | No demonstrated secret exposure or unauthorized network access was identified in the inspected application code. | Unsupported as a vulnerability | The reviewed code provided no evidence confirming such a vulnerability. |

The review was limited to the inspected project files. It is not a full security audit.

## 5. Risk Register

Scales: likelihood and impact are rated from 1 (low) to 3 (high). Risk score = likelihood × impact.

| ID | Cause → Event → Consequence | Component | L | I | Score | Mitigation / Owner | Verification | Residual risk |
|---|---|---|---:|---:|---:|---|---|---|
| R1 | Mutable internal object is returned → caller modifies it → stored expense data becomes incorrect. | ExpenseManager | 2 | 2 | 4 | Return a defensive copy. Owner: Developer. | Mutate returned dictionary and verify stored total remains unchanged. | Low |
| R2 | Non-finite numeric input is accepted → NaN/Infinity enters calculations → totals become unreliable. | Input validation | 2 | 3 | 6 | Reject non-finite values with `math.isfinite()`. Owner: Developer. | NaN and Infinity tests. | Low |
| R3 | No persistent storage → process exits → all recorded expenses are lost. | Data storage | 3 | 2 | 6 | Document limitation; consider file or database persistence in a future version. Owner: Product/Developer. | Inspect storage implementation and restart behavior. | Medium |
| R4 | Missing type validation → invalid values reach string methods → runtime exception. | Input validation | 2 | 2 | 4 | Add explicit type validation in a future change. Owner: Developer. | Add tests for None and non-string values. | Medium |
| R5 | EOF is not handled explicitly → input stream closes → CLI may terminate with an exception. | CLI | 2 | 1 | 2 | Handle EOFError gracefully in a future change. Owner: Developer. | Add a test for closed input. | Low |

### Priority risks

R1 and R2 were selected for immediate mitigation because both were confirmed and could directly compromise the correctness of expense data.

R3 remains an accepted limitation for this small demonstration application. It must be addressed before the application is used as a persistent financial record system.

## 6. Mitigation Records

### Mitigation 1 — R1: Protect stored expense data

**Change:** `add_expense()` returns a copy of the expense dictionary instead of exposing the internal dictionary.

**Regression test:** `test_mutating_add_expense_result_does_not_affect_manager`.

**Before:** The project had 11 passing tests after refactoring. The returned-object mutation scenario was not covered.

**After:** The new regression test passed; the complete suite passed 14/14 tests.

**Residual risk:** Low. Other future methods must also avoid exposing mutable internal state.

### Mitigation 2 — R2: Reject non-finite amounts

**Change:** Added `math.isfinite(amount)` validation before the positive amount check.

**Regression tests:**
- `test_reject_nan_amount`
- `test_reject_infinite_amount`

**Before:** A simple `amount <= 0` check did not reject NaN and positive Infinity.

**After:** Both new tests passed; the complete suite passed 14/14 tests.

**Residual risk:** Low for ordinary numeric inputs. Comprehensive type validation remains a separate improvement.

## 7. Pattern Decision: Strategy or Adapter

Two patterns were considered:

**Strategy:** Not applied. The application currently has one expense calculation and filtering approach. There are no interchangeable algorithms that justify introducing a strategy interface.

**Adapter:** Not applied. The application has no external service, incompatible API or alternative storage provider that needs an adapter.

Introducing either pattern would add unnecessary complexity to this small application.

A targeted structural refactoring was performed by encapsulating expense operations in `ExpenseManager`. This improves ownership of the expense collection and supports safer data handling, but it is not claimed to be a Strategy or Adapter implementation.

## 8. Agent Readiness Audit

Readiness score: **2/3 — Partially ready.**

| Criterion | Assessment |
|---|---|
| Project structure | Clear and small |
| README | Present with run and test instructions |
| AGENTS.md | Present with scope, safety and review rules |
| Installation | Python 3.10+; no third-party dependencies |
| Dependency pinning | Not applicable to the current standard-library-only implementation |
| Automated tests | Present; 14 tests passed |
| Linting | Not confirmed; no lint command was run |
| Static type checking | Not confirmed; no type checker was run |
| CI | Not confirmed; no CI execution was demonstrated |
| Build/package process | Not implemented or verified |
| Logging | No structured logging capability was verified |
| Security restrictions | Basic restrictions documented in AGENTS.md |
| Background-agent isolation | Documented in AGENT_SAFETY_PLAN.md |

The project is suitable for limited, supervised AI-assisted development. It is not fully prepared for autonomous or production-level agent workflows.

## 9. Background-Agent Safety Policy

The repository contains `AGENT_SAFETY_PLAN.md`.

Its main controls include:

- Work in a separate branch or isolated Git worktree.
- Do not modify the main branch directly.
- Restrict changes to approved project files.
- Allow only approved commands and read-only inspection by default.
- Prohibit secret access, production deployment and force-push.
- Require human approval for dependency changes, commits and pushes.
- Require a change summary, modified-file list, test output and Git diff.
- Stop and request human review if integration fails or unexpected data is encountered.
- Require human approval before destructive rollback operations.

## 10. Release Decision

**Decision: CONDITIONAL GO**

The application can be used as a local educational demonstration.

Reasons supporting this decision:

- The final automated test suite passed 14/14 tests.
- Two confirmed high-priority risks were mitigated and covered by regression tests.
- Project documentation and agent instructions are available.
- The repository was cleaned of unnecessary generated files.
- A background-agent safety policy was added.

Conditions and limitations:

- Expense records are not persistent.
- Some input type validation remains incomplete.
- EOF handling has not been verified or improved.
- CI, linting, static type checking, packaging and production deployment were not demonstrated.

The application is not approved for production financial record keeping without additional persistence, validation and operational controls.

## 11. AI Reflection

AI-assisted development made the review and improvement process more structured, but it also demonstrated why generated changes require independent verification. The initial project was small, so it was tempting to assume that passing unit tests meant the application was fully reliable. The risk review showed otherwise: returning a mutable internal dictionary could allow callers to alter stored expense data, while NaN and Infinity could bypass a basic positive-number check.

The AI-assisted refactoring introduced an ExpenseManager and expanded the test suite. However, the first attempt to add regression tests placed them outside the test class, meaning the test runner did not discover them. This was caught by comparing the expected test count with the actual output. The tests were then moved into the correct class and the suite passed with 14 tests. This reinforced the importance of checking actual test discovery rather than trusting an edit or a tool's description of its work.

The repository also contained generated files unrelated to the Python application. Cleaning these files and updating .gitignore improved the project structure. The AGENTS.md instructions and background-agent safety policy established boundaries for future AI work, including isolation, restricted commands and human approval.

Overall, AI was useful for identifying risks, proposing changes and preparing documentation. Human review remained essential for validating code, interpreting test results, resolving Git integration issues and deciding whether the application was ready for release. The final decision is conditional approval for educational use, not production use.

## 12. Deliverables and Evidence Appendix

Repository: https://github.com/nauryzb3k/sis05-expense-tracker

Project deliverables:

- `README.md`
- `AGENTS.md`
- `AGENT_SAFETY_PLAN.md`
- `expense_tracker.py`
- `test_expense_tracker.py`
- `.gitignore`
- `SIS05_REPORT.md` — this report

Evidence recorded during the work:

1. Baseline test run: 5 tests passed.
2. Post-refactoring test run: 11 tests passed.
3. Post-mitigation test run: 14 tests passed.
4. Git history records the baseline, refactoring, mitigations, repository cleanup and safety policy commits.
5. Git push output confirms that the commits were published to the remote `main` branch.

Only observed test results are reported. Checks that were not executed are explicitly marked as unverified.
