# Contributing

Use Python 3.12 or later and Claude Code 2.1.273 or later to validate a checkout:

```sh
python3 scripts/validate.py
claude plugin validate . --strict
claude plugin validate .claude-plugin/plugin.json --strict
claude plugin validate skills --strict
python3 scripts/package.py
```

The package is written to `dist/`. The validator checks manifests, skill inventory, source hashes, relative links, and Python syntax.

The cases in `evals/` use synthetic inputs to check skill selection and responses. To run them:

```sh
claude plugin eval . --trust-plugin --runs 1 --ablation none --no-publish --max-cost-usd 10
```

Evaluations consume Claude usage. They do not enable live MCP calls or verify authentication. Keep evaluation outputs, account data, and credentials out of commits and issue reports.

For connection troubleshooting, see [SETUP.md](SETUP.md). Include reproduction steps and relevant validation results with a pull request.
