# Claude directory submission

Status: **Not submitted — held for owner review.** The signed-in organization submission form is accessible. The new plugin's directory terms have not been accepted and the submission has not been sent. Version 1.0.0 is the published release; 1.0.1 is the review candidate with the Code/Cowork acceptance updates.

## Submission details

| Field | Value |
| --- | --- |
| Display name | GovTribe |
| Plugin identifier | `govtribe` |
| Version | `1.0.1` review candidate; `1.0.0` currently released |
| Publisher | GovTribe |
| Public repository | https://github.com/GovTribe/claude-plugin |
| Plugin path | Repository root (`.`) |
| Category | Productivity / research, using the closest available form category |
| Homepage | https://govtribe.com |
| Existing connector | https://claude.com/connectors/govtribe |
| Remote MCP | https://govtribe.com/mcp |
| Logo | `assets/govtribe-logo.png` (500 × 500 PNG) |
| License | Apache-2.0 |

Short description:

> Find government opportunities, research buyers and competitors, assess bids, analyze pricing, and prepare proposals with GovTribe data and guided workflows.

Audience and value:

> GovTribe is for government contractors and business-development teams using their existing GovTribe subscriptions in Claude. Five guided skills help customers research markets, qualify opportunities, examine individual records, reason about pricing and staffing, and prepare source-backed proposal materials. The plugin connects GovTribe's existing remote MCP service and preserves account permissions. Customers can ask in everyday language without writing code.

Requirements:

> A GovTribe account with MCP access and credits enabled, and a Claude plan/workspace permitting plugins and connectors. MCP operations may consume GovTribe credits. Users authenticate with GovTribe; no credentials are bundled. Python helpers are optional and have document/table fallbacks.

## Submit and verify

Use [the Claude organization form](https://claude.ai/admin-settings/directory/submissions/plugins/new) with directory management access, or [the Console form](https://platform.claude.com/plugins/submit) with Developer, Admin, or Owner access. Submit the public repository URL and its root plugin path. Use the logo and copy above if requested. Review any directory agreement in the form before accepting it.

After submission, record its identifier, date, submitted commit, and actual review status here. Confirm the submission appears in the [organization directory submissions](https://claude.ai/admin-settings/directory/submissions). Do not mark the plugin accepted or installable from an Anthropic catalog until that state is verified.

## Official catalog distinction

As checked September 16, 2026, [Claude Code's submission documentation](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-community-marketplace) sends third-party submissions to `claude-community`, backed by `anthropics/claude-plugins-community`. It states that `claude-plugins-official` is curated separately and has no application process. The [Claude.ai submission guide](https://claude.com/docs/plugins/submit) still describes the directory differently. Both point to the same submission forms. Follow the form's actual review result and do not promise either official-catalog placement or an Anthropic Verified badge.

GovTribe's existing connector listing is a separate listing and does not automatically publish this plugin. Customers can use the GovTribe repository marketplace or release ZIP while directory review is pending.

## Existing connector maintenance

The existing published MCP listing was updated separately with the current 112 tool names, clearer permissions, MCP App and self-test declarations, company details, the supplied SVG logo URL, and simpler reviewer setup instructions. Those listing changes are pending Anthropic review; they do not constitute submission of this plugin. Reviewer credentials are held only in the private testing-access form and are not included in this repository or package.
