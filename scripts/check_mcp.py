#!/usr/bin/env python3
"""Check public OAuth discovery and unauthenticated MCP rejection; no credentials are used."""

import argparse
import json
import sys
from urllib.error import HTTPError
from urllib.request import HTTPRedirectHandler, Request, build_opener

ENDPOINT = "https://govtribe.com/mcp"


class NoRedirects(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    opener = build_opener(NoRedirects())
    opener.addheaders = [("User-Agent", "GovTribe-Claude-Plugin-Check/1.0")]
    for suffix in ("oauth-protected-resource/mcp", "oauth-authorization-server/mcp"):
        with opener.open(f"https://govtribe.com/.well-known/{suffix}", timeout=30) as response:
            metadata = json.load(response)
        if suffix.startswith("oauth-protected"):
            assert metadata["resource"] == ENDPOINT
            assert ENDPOINT in metadata["authorization_servers"]
        else:
            assert metadata["issuer"] == ENDPOINT
            assert "S256" in metadata["code_challenge_methods_supported"]
            for key in ("authorization_endpoint", "token_endpoint", "registration_endpoint"):
                assert metadata[key].startswith("https://govtribe.com/")
    print("OAuth resource and authorization discovery: passed")
    payload = {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
        "protocolVersion": "2025-03-26", "capabilities": {},
        "clientInfo": {"name": "govtribe-plugin-check", "version": "1.0.0"},
    }}
    request = Request(ENDPOINT, data=json.dumps(payload).encode(), headers={
        "Content-Type": "application/json", "Accept": "application/json, text/event-stream",
    }, method="POST")
    try:
        with opener.open(request, timeout=45):
            raise RuntimeError("Expected the unauthenticated MCP request to be rejected")
    except HTTPError as error:
        if error.code != 401:
            raise
        error.close()
    print("Unauthenticated MCP request correctly rejected (401)")
    print("For authenticated tools, connect GovTribe through your Claude client's OAuth flow.")


if __name__ == "__main__":
    try:
        main()
    except HTTPError as error:
        sys.exit(f"MCP check failed with HTTP {error.code}; response omitted.")
    except Exception as error:
        sys.exit(f"MCP check failed: {type(error).__name__}: {error}")
