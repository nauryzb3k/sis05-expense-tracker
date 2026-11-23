# Background-Agent Safety Policy

## 1. Isolation
- Every background agent must work in a separate Git branch or isolated worktree.
- Agents must not modify the main branch directly.
- Changes must be submitted for human review before merging.

## 2. Allowed Files
- expense_tracker.py
- test_expense_tracker.py
- README.md
- AGENTS.md
- .gitignore
- Documentation files explicitly approved by the human reviewer.

## 3. Allowed Commands
- python -m unittest -v
- python expense_tracker.py
- git status
- git diff
- git log
- Other read-only inspection commands.

## 4. Prohibited Actions
- Accessing, displaying, or transmitting secrets or private data.
- Production deployment.
- git push --force.
- Destructive file or repository operations.
- Installing, removing, or updating dependencies without approval.
- Modifying files outside the repository.
- Committing or pushing without explicit human approval.
- Changing Git configuration or remote settings without approval.

## 5. Time and Scope Limits
- Each task must have a clearly defined objective and file scope.
- Stop when the requested task is complete or the agreed time limit is reached.
- Ask for human approval before expanding the scope.

## 6. Required Artifacts
- Summary of changes.
- List of modified files.
- Test commands and actual outputs.
- Git diff for review.
- Known limitations and unresolved risks.

## 7. Human Review
- A human must inspect all changes and diffs.
- Tests must be executed and results reported accurately.
- No changes are accepted or merged without explicit approval.

## 8. Failure Handling and Rollback
- Stop work if unexpected files or sensitive data are encountered.
- Do not attempt destructive recovery automatically.
- Preserve logs and report the failure.
- Use Git restore, branch deletion, or worktree removal only after human approval.
- If integration fails, stop and request human review; never force-push.
