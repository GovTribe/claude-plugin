![GovTribe](assets/govtribe-logo.png)

# GovTribe

Claude plugin containing the GovTribe MCP connection and seven government contracting skills.

## Requirements

- A GovTribe account with MCP access and credits enabled.
- A Claude plan and workspace that permit plugins and connectors.

MCP calls may consume GovTribe credits. Access to data and workspace actions follows your GovTribe account permissions.

## Installation

### Claude web, desktop, and Cowork

1. Open [GovTribe in the Claude plugin directory](https://claude.ai/customize/plugins/id/plugin_01H6qRziGtLHCr56JPBWyq82) and add the plugin.
2. Open **Customize → Connectors**, select [GovTribe](https://claude.com/marketplace/connectors/govtribe), and complete sign-in and authorization. Reuse an existing GovTribe connection if one is already connected.
3. Start a new conversation. Select a skill from the `/` or `+` menu, or describe the task in your message.

For manual installation, download the plugin ZIP from [Releases](https://github.com/GovTribe/claude-plugin/releases/latest), keep it zipped, and upload it in **Customize → Plugins**. For Cowork, open the Cowork tab first. The directory version may lag the repository while a new release is under review.

Where **Add marketplace** is available, add `https://github.com/GovTribe/claude-plugin` and install **GovTribe**. Marketplace installations support repository updates; ZIP installations are updated by uploading a newer release.

Plugin availability depends on your Claude plan, workspace settings, and app version. See [Claude's plugin installation guide](https://support.claude.com/en/articles/13837440-use-plugins-in-claude).

### Claude Code

Run these commands inside Claude Code:

```text
/plugin marketplace add GovTribe/claude-plugin
/plugin install govtribe@govtribe
```

Open `/mcp`, select the GovTribe server, and complete sign-in and authorization in your browser. Start a new session after connecting.

If GovTribe is already connected through your Claude.ai account, the skills can reuse that connection when Code is signed in to the same account. See [connection troubleshooting](SETUP.md) for authentication options and API-key session requirements.

## Skills

| Skill | Scope |
| --- | --- |
| `govtribe-market-intelligence` | Market sizing, buyers, vendors, forecasts, recompetes, and individual-record Deep Dive research |
| `govtribe-capture-workflows` | Opportunity discovery, pipeline, bid/no-bid, incumbents, competitors, and teaming |
| `govtribe-pricing-data` | Labor rates, staffing, pricing models, and price-to-win evidence |
| `govtribe-proposal-workflows` | Solicitation extraction, compliance matrices, outlines, and proposal documents |
| `govtribe-file-templates` | Templates for documents, workbooks, and presentations |
| `govtribe-govcon-writing` | Source-backed proposal narratives, RFI replies, and official correspondence |
| `govtribe-docs` | GovTribe product guides, data definitions, query guidance, and MCP tool documentation |

In Claude Code, skills use the `/govtribe:` prefix, for example `/govtribe:govtribe-market-intelligence`.

Example requests:

- “Find NASA's federal agency record in GovTribe and cite the source.”
- “Calculate the FTEs required for 36,000 annual labor hours at 1,800 productive hours per FTE.”
- “Build a compliance checklist from this solicitation and its amendments.”
- “Choose a template for our capture brief and adapt it using these sources.”
- “Apply these review comments to the selected document and check the saved revision.”

The plugin connects to `https://govtribe.com/mcp`. Available tools depend on the connected account and client. Skills include reference guides, templates, and optional Python helpers for document and spreadsheet outputs. Workspace changes and outbound messages require a user request.

## Support, privacy, and license

- [Connection troubleshooting](SETUP.md)
- [GovTribe MCP documentation](https://govtribe.com/docs/govtribe-user-guide/govtribe-mcp/)
- [GovTribe support](https://govtribe.com/docs/govtribe-user-guide/contact-govtribe/)
- [Plugin issues](https://github.com/GovTribe/claude-plugin/issues)
- [Privacy policy](https://www.govexec.com/about/privacy-policy/) and [MCP data handling](https://govtribe.com/docs/govtribe-user-guide/ai-data-handling-and-subprocessors/)

Do not include credentials or private account data in GitHub issues. The plugin is licensed under [Apache-2.0](LICENSE). GovTribe service access is subject to the [GovTribe Terms of Use](https://govtribe.com/docs/govtribe-user-guide/terms-of-use/).

## Prepared seven-skill update

This 1.2.0 release candidate contains Market Intelligence (including Deep Dive), Capture, Pricing, Proposal Workflows, File Templates, GovCon Writing and GovTribe Docs. This directory-validation experiment retains 14 unchanged template masters and omits Annotated Proposal Outline. Outline research remains available through Proposal Workflows and native authoring. See [candidate provenance](docs/provenance.md) for integrity checks and known limitations. This branch is for review; it does not publish 1.2.0.
