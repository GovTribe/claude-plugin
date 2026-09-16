# Connection troubleshooting

## Connect GovTribe

1. Confirm that your GovTribe account has MCP access and credits enabled.
2. In Claude, open **Customize → Connectors**, select **GovTribe**, and complete sign-in and authorization.
3. Start a new conversation and ask: “Use GovTribe to find its guide to federal award values.” A documentation result confirms that the connection can read from GovTribe.

See the [GovTribe connection guide](https://govtribe.com/docs/govtribe-user-guide/govtribe-mcp/connect-govtribe-to-claude/) for additional setup instructions.

## Claude Code

Sign in to Claude Code with the same Claude.ai account used to connect GovTribe. Restart Code and open `/mcp`. A connected **claude.ai GovTribe** entry can supply tools to the plugin even if a separate `plugin:govtribe:govtribe` entry needs authentication.

### Native sign-in returns `invalid_redirect_uri`

GovTribe currently rejects the local callback used by a fresh native Claude Code connection. Use the connected Claude.ai account above. Reinstalling the plugin does not resolve this server-side error.

Code sessions authenticated with an Anthropic API key or another provider do not inherit Claude.ai connectors. For bearer-token configuration, follow [GovTribe's MCP server setup](https://govtribe.com/docs/govtribe-user-guide/govtribe-mcp/mcp-server-urls/). Enter credentials only in the client's secure configuration or sign-in interface, never in a conversation or repository.

See [Claude Code's connector documentation](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claudeai) for account and connection requirements.

## Missing tools or access denied

- Reconnect GovTribe, then start a new conversation.
- Check your GovTribe account's MCP access, credits, and permissions.
- Check whether your Claude workspace administrator permits the connector and plugin.
- If Plugins is unavailable, check your plan, workspace settings, and app version.

For unresolved connection issues, contact [GovTribe support](https://govtribe.com/docs/govtribe-user-guide/contact-govtribe/). Include the client, error message, and approximate time of the failure; exclude credentials and private account data.
