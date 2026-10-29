# Directory review notes

The plugin declares one remote MCP connection to GovTribe. Users authorize it
through their Claude client's OAuth flow. It has no install hooks or local MCP
server and does not read credentials from the user's environment.

`scripts/check_mcp.py` is an optional, manually run diagnostic. It reads public
OAuth discovery and checks that an unauthenticated request is rejected. It does
not authenticate, read workspace data or run during installation. Authenticated
tool checks belong in the connected Claude client.

The pinned Claude CLI commands in the GitHub Actions workflow validate the
repository in CI; they are not plugin installation or runtime commands. Template
previews are images for visual reference and checksum verification, not code.

The manifest declares the GovExec privacy policy and an existing 1000-pixel
GovTribe PNG icon. Directory listing fields are ignored by Claude Code at runtime.

Office template binaries remain present in the main release candidate. They can
require an Anthropic reviewer under the directory's file policy. These metadata
and diagnostic fixes do not claim that the binary inspection hold has cleared.

See [Anthropic's pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist)
and [directory manifest fields](https://code.claude.com/docs/en/plugins-reference#directory-listing-fields).
