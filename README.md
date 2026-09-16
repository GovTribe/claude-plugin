<img src="assets/govtribe-logo.png" alt="GovTribe" width="96" />

# GovTribe

Turn government contracting questions into source-backed research and practical next steps in Claude. GovTribe combines the [GovTribe connector](https://claude.com/connectors/govtribe) with five guided workflows for customers pursuing public-sector business.

Ask in everyday language. You do not need to know tool names or write code.

| What you need | Try asking Claude |
| --- | --- |
| Market intelligence | “Which agencies buy cybersecurity services like ours, and what contracts may recompete next year?” |
| Capture and pipeline | “Analyze this opportunity and recommend whether we should pursue it.” |
| Pricing and staffing | “Is 46 FTEs reasonable for this scope? Show the assumptions that matter.” |
| A detailed research brief | “Deep dive this vendor: customers, awards, vehicles, and upcoming recompetes.” |
| Proposal preparation | “Build a compliance checklist for this solicitation, including amendments and submission requirements.” |

## Before you start

You need a GovTribe account with MCP access and credits enabled, and a paid Claude plan that allows plugins and connectors. GovTribe MCP usage may consume your GovTribe credits. Your existing account permissions still apply.

## Install in Claude

### Web, desktop, and Cowork

1. Download **govtribe-1.0.0.zip** from [Releases](https://github.com/GovTribe/claude-plugin/releases/latest). Keep it zipped.
2. In Claude, open **Customize → Plugins** and use the upload option to select that file. In Cowork, open the Cowork tab first.
3. Open the plugin's **GovTribe** connector and choose **Connect**. Sign in to your GovTribe account and complete the authorization prompt. If GovTribe is already connected, use the existing connection.
4. Start a new conversation and try one of the questions above. You can also type `/` or use the `+` menu to choose a workflow.

If the plugin's connector does not offer a connection control, add the existing [GovTribe connector](https://claude.com/connectors/govtribe) through **Customize → Connectors**, then connect it. Follow the [GovTribe connection guide](https://govtribe.com/docs/govtribe-user-guide/govtribe-mcp/connect-govtribe-to-claude/).

Where **Add marketplace** is available, you can instead add `https://github.com/GovTribe/claude-plugin`, then install **GovTribe**. This supports updates from this repository. A ZIP installation can be updated by uploading the newer release.

Claude's [current help article](https://support.claude.com/en/articles/13837440-use-plugins-in-claude) describes plugins in web chat, desktop chat, and Cowork. Availability can depend on your workspace settings and app version. If Plugins is unavailable, update Claude or ask your workspace administrator; the GovTribe connector can still be used wherever your account supports it.

### Claude Code

Run these commands inside Claude Code:

```text
/plugin marketplace add GovTribe/claude-plugin
/plugin install govtribe@govtribe
```

Connect GovTribe in **Claude.ai → Customize → Connectors**, then sign in to Claude Code with the same Claude.ai account. Restart Code and use `/mcp` to confirm **claude.ai GovTribe** is connected. The plugin's skills can use that connection. This is the setup verified with live calls on September 16, 2026.

Fresh authentication of the plugin's separate Code server currently fails with `invalid_redirect_uri` because GovTribe does not yet accept Code's local callback. A server fix is being prepared; use the connected Claude.ai account in the meantime. API-key-only Claude Code sessions do not inherit Claude.ai connectors; see [SETUP.md](SETUP.md) for the developer path and verification limits.

The plugin's identifier is `govtribe`; its display name is **GovTribe**. Its five skills are also available as `/govtribe:govtribe-market-intelligence`, `/govtribe:govtribe-capture-workflows`, `/govtribe:govtribe-pricing-data`, `/govtribe:govtribe-deep-dive`, and `/govtribe:govtribe-proposal-workflows`.

For account connection problems, see [SETUP.md](SETUP.md). Never paste an API key into a conversation.

## What is included

Five skills, their reference guides, templates and optional Python helpers, and one remote MCP connection to `https://govtribe.com/mcp`. The connection uses the standard GovTribe server, so Claude discovers the available tools from the service instead of relying on a fixed tool list in this plugin.

The workflows distinguish source facts from assumptions, preserve solicitation amendments and record relationships, and explain missing evidence. Workspace changes and outbound messages require a user request. Optional document and spreadsheet helpers use Claude's file capabilities when available, with Markdown or CSV fallbacks.

Installing the plugin does not create a GovTribe subscription or grant access beyond your account. The plugin includes no background hooks, local MCP server, bundled credentials, or automatic workspace changes.

## Directory availability

This repository is the GovTribe-maintained distribution. Directory submission and review status are recorded in [docs/submission.md](docs/submission.md). A submission does not imply acceptance or an Anthropic Verified badge.

## Development

```sh
python3 scripts/validate.py
claude plugin validate . --strict
claude plugin validate .claude-plugin/plugin.json --strict
python3 scripts/package.py
claude --plugin-dir .
```

See [docs/verification.md](docs/verification.md) for behavioral evals, connection checks, and verification limits. Increment the manifest version for every published update. See [docs/provenance.md](docs/provenance.md) for the source of the five skills.

## Support and license

For account access and data questions, use [GovTribe support](https://govtribe.com/docs/govtribe-user-guide/contact-govtribe/). Report plugin packaging issues in [GitHub Issues](https://github.com/GovTribe/claude-plugin/issues) without including account data or credentials.

The plugin is licensed under [Apache-2.0](LICENSE). GovTribe service access is governed by GovTribe's terms.
