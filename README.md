# Pre-commit hooks #

Hooks for your bug & issue tracker.

### Using pre-commit-hooks with pre-commit ###


Add this to your `.pre-commit-config.yaml`:
```
  - repo: https://github.com/DanyloSolohub/prehooks
    rev: 1.0.0
    hooks:
      - id: task_id-in-branch-name
      - id: add-msg-issue-prefix
```

### Hooks available ###

___task_id-in-branch-name___

Allow only branches containing the issue ID

* Branch should pass regex: `(^[0-9A-Za-z_]+-[0-9]+)\/[a-zA-Z0-9._-]+$`. 
* Example: `PROJ-123/short_description`

* Whitelist: `'master', 'main', 'staging', 'develop'`

___add-msg-issue-prefix___

Searches the branch name for something looking like a jira issue name and prepends the commit message with it

* Take issue ID from branch and add it in your commit

* Example: your commit message is: `added some important logic` and your branch: `PROJ-123/short_description` , hook will modify commit message to: `[PROJ-123] added some important logic`

### Troubleshoot ###

If you enabled `add-msg-issue-prefix` in your `.pre-commit-config.yaml` but you don't see it, try installing `prepare-commit-msg` hook type directly, using:
`pre-commit install --hook-type prepare-commit-msg`


