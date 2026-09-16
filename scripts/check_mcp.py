#!/usr/bin/env python3
"""Read-only GovTribe MCP smoke check. Never prints credentials or tool payloads."""

import argparse
import json
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
ENDPOINT = "https://govtribe.com/mcp"


class NoRedirects(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--authenticated", action="store_true",
                        help="Use GOVTRIBE_MCP_ACCESS_TOKEN from the environment for tools/list and a Documentation read")
    args = parser.parse_args()
    token = os.environ.get("GOVTRIBE_MCP_ACCESS_TOKEN") if args.authenticated else None
    if args.authenticated and not token:
        sys.exit("Set GOVTRIBE_MCP_ACCESS_TOKEN in your terminal environment; never paste it into chat.")
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
    headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request_id = 0

    def rpc(method, params=None, notification=False):
        nonlocal request_id
        request_id += 1
        payload = {"jsonrpc": "2.0", "method": method}
        if not notification:
            payload["id"] = request_id
        if params is not None:
            payload["params"] = params
        request = Request(ENDPOINT, data=json.dumps(payload).encode(), headers=headers, method="POST")
        with opener.open(request, timeout=45) as response:
            if response.headers.get("Mcp-Session-Id"):
                headers["Mcp-Session-Id"] = response.headers["Mcp-Session-Id"]
            raw = response.read().decode()
        if notification:
            return None
        if raw.lstrip().startswith("{"):
            message = json.loads(raw)
        else:
            messages = [json.loads(line[5:].strip()) for line in raw.splitlines() if line.startswith("data:")]
            message = next(m for m in messages if m.get("id") == request_id)
        if "error" in message:
            raise RuntimeError(f"{method} returned an MCP error; payload omitted")
        return message["result"]

    try:
        initialized = rpc("initialize", {"protocolVersion": "2025-03-26", "capabilities": {},
                                          "clientInfo": {"name": "govtribe-plugin-check", "version": "1.0.0"}})
    except HTTPError as error:
        if not token and error.code == 401:
            print("Unauthenticated MCP request correctly rejected (401)")
            print("Authenticated session not tested; run --authenticated with your own environment token.")
            return
        raise
    if not token:
        raise RuntimeError("Expected authentication to be required")
    headers["MCP-Protocol-Version"] = initialized["protocolVersion"]
    rpc("notifications/initialized", notification=True)
    tools = []
    cursor = None
    for _ in range(100):
        result = rpc("tools/list", {"cursor": cursor} if cursor else {})
        tools.extend(result["tools"])
        cursor = result.get("nextCursor")
        if not cursor:
            break
    else:
        raise RuntimeError("Tool catalog pagination did not finish")
    required = {"Documentation"}
    for path in (ROOT / "skills").rglob("*.md"):
        required.update(re.findall(r"`([A-Z][A-Za-z]+(?:_[A-Z][A-Za-z0-9]*)+)`", path.read_text()))
    missing = required - {tool["name"] for tool in tools}
    if missing:
        raise RuntimeError("Referenced tools missing from live catalog: " + ", ".join(sorted(missing)))
    result = rpc("tools/call", {"name": "Documentation", "arguments": {
        "query": "federal award values and transactions", "limit": 1, "max_tokens": 500}})
    if result.get("isError") or not result.get("content"):
        raise RuntimeError("Documentation read did not return successful content")
    print(f"Authenticated initialize, {len(tools)} tool definitions, {len(required)} referenced operations, and Documentation read: passed")


if __name__ == "__main__":
    try:
        main()
    except HTTPError as error:
        sys.exit(f"MCP check failed with HTTP {error.code}; response omitted to protect account data.")
    except Exception as error:
        sys.exit(f"MCP check failed: {type(error).__name__}: {error}")
