# Verification

## Reproduce local checks

```sh
python3 scripts/validate.py
npx --yes @anthropic-ai/claude-code@2.1.273 plugin validate . --strict
npx --yes @anthropic-ai/claude-code@2.1.273 plugin validate .claude-plugin/plugin.json --strict
npx --yes @anthropic-ai/claude-code@2.1.273 plugin validate skills --strict
python3 scripts/package.py
claude --plugin-dir . plugin details govtribe
claude --plugin-dir ./dist/govtribe-1.0.1.zip plugin details govtribe
```

The local validator checks the five-skill inventory, original-source hashes for unmodified files, relative reference links, Python syntax, JSON, MCP configuration, and absence of machine-specific paths. The packager includes only installation files, skills, logo, and documentation; it excludes Git metadata, local settings, eval transcripts, credentials, and build files. ZIP members have stable timestamps and permissions.

## Behavioral evals

The seven cases under `evals/` cover all five workflows, an unrelated request, and a disconnected GovTribe account. They use synthetic user-supplied facts to check routing, arithmetic, award-value semantics, mandatory bid gates, incumbent uncertainty, amendment precedence, and embedded malicious instructions.

Run with Claude Code 2.1.273 (or a later version supporting plugin evals), using an authenticated Claude account:

```sh
npx --yes @anthropic-ai/claude-code@2.1.273 plugin eval . \
  --trust-plugin --runs 1 --ablation none --no-publish --max-cost-usd 10
```

For stronger routing and outcome confidence, run three trials with the no-plugin baseline:

```sh
npx --yes @anthropic-ai/claude-code@2.1.273 plugin eval . \
  --trust-plugin --runs 3 --ablation with-without --no-publish --max-cost-usd 30
```

Evals consume Claude plan usage or API billing. They grant only read-only built-ins; real MCP servers and workspace writes are not enabled. This suite evaluates reasoning from controlled evidence, not live OAuth or GovTribe search correctness. Keep `evals/results/` private and untracked. See [Claude's eval documentation](https://code.claude.com/docs/en/plugin-evals).

## Authenticated acceptance checks

In an isolated Claude session, install the released ZIP or the repository marketplace. Verify that the UI shows GovTribe, five skills, and its connector. Connect the intended GovTribe account through the user interface; run a `Documentation` read and one public-record search. Confirm returned sources are cited. Run a representative question from each workflow, and verify normal chat as well as Cowork where available.

These checks require a signed-in Claude browser session and GovTribe authorization. An authenticated call through a different host's existing connector is supporting MCP evidence; it does not prove this plugin's Claude login flow.

`python3 scripts/check_mcp.py` checks public OAuth discovery and authentication enforcement. `python3 scripts/check_mcp.py --authenticated` also initializes MCP, checks the live tool catalog against referenced operations, and performs a bounded Documentation read using `GOVTRIBE_MCP_ACCESS_TOKEN` from the terminal environment. It never prints the token or returned account data. If your Python installation lacks a certificate bundle, configure its trusted CA bundle (on this macOS host, `SSL_CERT_FILE=/etc/ssl/cert.pem`); do not disable TLS verification.

## Observed results

Checks performed September 16, 2026:

- Claude Code 2.1.258 and 2.1.273 recognized GovTribe, all five skills, and one remote MCP server. Strict marketplace, plugin, and component validation passed on 2.1.273.
- A clean temporary Claude configuration successfully added the local marketplace and installed `govtribe@govtribe`. The release ZIP independently loaded the same component inventory.
- All 157 imported skill files matched the completed portable release before the documented adaptations. Relative links, all 11 Python helper entrypoints, deterministic ZIP generation, and archive contents passed checks. Five broken proposal template links were repaired.
- The included deep-dive sample passed its dossier validator. The bid/no-bid and black-hat engines' demo outputs passed their corresponding validators.
- The live GovTribe OAuth metadata resolved with PKCE support, and an unauthenticated MCP initialization returned HTTP 401. Claude Code recognized the plugin's server as needing authentication.
- All 74 referenced multiword tool operations were present in the existing connected GovTribe catalog. A bounded authenticated `Documentation` read succeeded through that existing connector. This was a Codex connector call, not a Claude plugin authentication test.
- All seven behavioral cases passed in their latest scoped runs (13 successful trials total): capture, proposal, and unrelated writing each passed 3/3; market, pricing, deep dive, and disconnected-account behavior each passed 1/1. See [eval-summary.json](eval-summary.json). These runs used the account default model, read-only tools, no real MCP servers, and no no-plugin baseline; they do not establish a measured improvement over base Claude.
- The initial seven-case run passed all outcome rubrics but skipped the capture and proposal skills. Their descriptions were revised. Proposal repeats then exposed an ambiguous test fixture (replacement of an entire section versus only two fields) and an overly broad grader; the fixture and rubric were clarified without changing the intended assertions. The proposal skill also now explicitly separates source-mandated rules from recommended checks. All final proposal trials passed.

## Live Claude acceptance

The published 1.0.0 ZIP was uploaded through Claude's private plugin upload interface on September 16, 2026. Claude displayed GovTribe, five skills, and one connected GovTribe connector. These checks reused an existing authorized Claude.ai GovTribe connection.

| Surface | Observed result |
| --- | --- |
| Claude web chat | Loaded the deep-dive skill and agency reference; Documentation and Search Federal Agencies returned NASA's real agency record and source URL. |
| Cowork in Claude web | Loaded the pricing skill and reference, retrieved live GovTribe Documentation, and correctly calculated a synthetic 20-FTE requirement, 5-FTE staffing gap, $88 hourly price, and $3,168,000 annual price. |
| Claude Code 2.1.273 | The connected Claude.ai GovTribe server completed Documentation and NASA agency reads. A separate natural-language pricing request automatically selected the pricing skill and produced the expected arithmetic. |
| Fresh native Claude Code OAuth | Failed at dynamic client registration with HTTP 400 `invalid_redirect_uri`. A GovTribe server hotfix is being prepared; the tested interim path is the existing Claude.ai connection described in [SETUP.md](../SETUP.md). |

The current Claude connector exposes 112 named tools: 111 ordinary tools and one app-only document refresh tool. Tool availability remains subject to the account and client.

The 1.0.1 review candidate adds explicit discovery of an existing working GovTribe connection before declaring authentication unavailable, and converts Documentation `/docs/` citations to absolute GovTribe URLs. The published 1.0.0 archive is unchanged.

A follow-up Code run loaded the packaged 1.0.1 pricing skill, found the working Claude.ai connector, retrieved live Documentation, returned the expected staffing and price calculations, and cited absolute `https://govtribe.com/docs/` links. A separate bounded diagnostic made successful read-only calls to State and Local Contract Opportunities, BLS Occupational Wage Data, Federal Grant Opportunities, and Federal Agencies. These four successful requests establish point-in-time availability, not an explanation or resolution of historical tool errors.

Fresh native OAuth after the server deployment and the native desktop application UI remain unverified. The live checks cover representative read-only workflows, not every tool or production write action. Directory submission is held for owner review; its status is tracked in [submission.md](submission.md).
