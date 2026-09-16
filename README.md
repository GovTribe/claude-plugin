<img src="assets/govtribe-logo.png" alt="GovTribe" width="96" />

# GovTribe

Claude plugin containing the GovTribe MCP connection and five government contracting skills.

## Requirements

- A GovTribe account with MCP access and credits enabled.
- A Claude plan and workspace that permit plugins and connectors.

MCP calls may consume GovTribe credits. Access to data and workspace actions follows your GovTribe account permissions.

## Installation

### Claude web, desktop, and Cowork

1. Download the plugin ZIP from [Releases](https://github.com/GovTribe/claude-plugin/releases/latest). Keep the file zipped.
2. Open **Customize → Plugins** in Claude and upload the ZIP. For Cowork, open the Cowork tab first.
3. Open **Customize → Connectors**, select [GovTribe](https://claude.com/connectors/govtribe), and complete sign-in and authorization. Reuse an existing GovTribe connection if one is already connected.
4. Start a new conversation. Select a skill from the `/` or `+` menu, or describe the task in your message.

Where **Add marketplace** is available, add `https://github.com/GovTribe/claude-plugin` and install **GovTribe**. Marketplace installations support repository updates; ZIP installations are updated by uploading a newer release.

Plugin availability depends on your Claude plan, workspace settings, and app version. See [Claude's plugin installation guide](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

### Claude Code

Run these commands inside Claude Code:

```text
/plugin marketplace add GovTribe/claude-plugin
/plugin install govtribe@govtribe
```

Connect GovTribe in **Claude.ai → Customize → Connectors**, then sign in to Claude Code with the same Claude.ai account. Restart Code and use `/mcp` to confirm **claude.ai GovTribe** is connected.

If the plugin's separate connection reports `invalid_redirect_uri`, use the Claude.ai connection above. See [connection troubleshooting](SETUP.md) for details and API-key session requirements.

## Skills

| Skill | Scope |
| --- | --- |
| `govtribe-market-intelligence` | Market sizing, buyers, vendors, forecasts, and recompetes |
| `govtribe-capture-workflows` | Opportunity discovery, pipeline, bid/no-bid, incumbents, competitors, and teaming |
| `govtribe-pricing-data` | Labor rates, staffing, pricing models, and price-to-win evidence |
| `govtribe-deep-dive` | Research on an individual opportunity, award, agency, vendor, program, or jurisdiction |
| `govtribe-proposal-workflows` | Solicitation extraction, compliance matrices, outlines, and proposal documents |

In Claude Code, skills use the `/govtribe:` prefix, for example `/govtribe:govtribe-deep-dive`.

Example requests:

- “Find NASA's federal agency record in GovTribe and cite the source.”
- “Calculate the FTEs required for 36,000 annual labor hours at 1,800 productive hours per FTE.”
- “Build a compliance checklist from this solicitation and its amendments.”

The plugin connects to `https://govtribe.com/mcp`. Available tools depend on the connected account and client. Skills include reference guides, templates, and optional Python helpers for document and spreadsheet outputs. Workspace changes and outbound messages require a user request.

## Support, privacy, and license

- [Connection troubleshooting](SETUP.md)
- [GovTribe MCP documentation](https://govtribe.com/docs/govtribe-user-guide/govtribe-mcp/)
- [GovTribe support](https://govtribe.com/docs/govtribe-user-guide/contact-govtribe/)
- [Plugin issues](https://github.com/GovTribe/claude-plugin/issues)
- [Privacy policy](https://govtribe.com/docs/govtribe-user-guide/privacy-policy/) and [MCP data handling](https://govtribe.com/docs/govtribe-user-guide/ai-data-handling-and-subprocessors/)

Do not include credentials or private account data in GitHub issues. The plugin is licensed under [Apache-2.0](LICENSE). GovTribe service access is subject to the [GovTribe Terms of Use](https://govtribe.com/docs/govtribe-user-guide/terms-of-use/).
