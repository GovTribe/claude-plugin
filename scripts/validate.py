#!/usr/bin/env python3
"""Validate the releasable GovTribe plugin without network access or dependencies."""

import ast
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {
    "govtribe-capture-workflows", "govtribe-deep-dive",
    "govtribe-market-intelligence", "govtribe-pricing-data",
    "govtribe-proposal-workflows",
}


def validate(root=ROOT):
    errors = []

    def check(condition, message):
        if not condition:
            errors.append(message)

    def read_json(path):
        try:
            return json.loads((root / path).read_text())
        except (OSError, ValueError) as exc:
            errors.append(f"{path}: {exc}")
            return {}

    plugin = read_json(".claude-plugin/plugin.json")
    check(plugin.get("name") == "govtribe", "Plugin identifier must be govtribe")
    check(plugin.get("displayName") == "GovTribe", "Plugin display name must be GovTribe")
    check(bool(re.fullmatch(r"\d+\.\d+\.\d+", plugin.get("version", ""))), "Invalid release version")
    check(plugin.get("skills") == "./skills/", "Root marketplace plugin must explicitly declare skills")
    check(not any(k in plugin for k in ("hooks", "agents", "dependencies")), "Unexpected executable components")
    mcp = read_json(".mcp.json")
    check(mcp == {"mcpServers": {"govtribe": {"type": "http", "url": "https://govtribe.com/mcp"}}},
          "Expected only the public remote GovTribe server, without bundled credentials")
    marketplace = read_json(".claude-plugin/marketplace.json")
    entries = marketplace.get("plugins", [])
    check(len(entries) == 1 and entries[0].get("name") == "govtribe" and entries[0].get("source") == "./",
          "Marketplace must resolve the plugin at the repository root")
    check(bool(marketplace.get("description")), "Marketplace description is required")
    check(not (root / "hooks").exists(), "Unexpected hook directory")
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    check({p.parent.name for p in skills} == EXPECTED_SKILLS, "Expected exactly the five GovTribe skills")
    for path in skills:
        body = path.read_text()
        match = re.match(r"\A---\n(.*?)\n---\n", body, re.S)
        check(bool(match), f"Missing frontmatter: {path.relative_to(root)}")
        if match:
            check(f"name: {path.parent.name}" in match[1], f"Skill name mismatch: {path}")
            check(bool(re.search(r"^description: .+", match[1], re.M)), f"Missing description: {path}")
    for path in (root / "skills").rglob("*"):
        check(not path.is_symlink(), f"Symlink in skills: {path}")
        check(path.name not in {".DS_Store", "__pycache__"}, f"Unwanted generated file: {path}")
        if not path.is_file():
            continue
        if path.suffix == ".json":
            read_json(path.relative_to(root))
        if path.suffix == ".py":
            try:
                ast.parse(path.read_text(), filename=str(path))
            except SyntaxError as exc:
                errors.append(str(exc))
        if path.suffix in {".md", ".py", ".json"}:
            body = path.read_text()
            check(not re.search(r"/Users/|/home/[^/\s]+/|/mnt/data/", body), f"Machine-specific path: {path}")
        if path.suffix == ".md":
            for link in re.findall(r"\]\(([^)]+)\)", body):
                target = unquote(link.split("#", 1)[0].split(" ", 1)[0].strip("<>"))
                if not target or urlsplit(target).scheme or target.startswith("/"):
                    continue
                resolved = (path.parent / target).resolve()
                check(resolved.is_relative_to(root.resolve()) and resolved.exists(),
                      f"Broken or escaping relative link: {path.relative_to(root)} -> {target}")
    provenance = read_json("docs/skill-source.json")
    originals = provenance.get("files", {})
    adaptations = set(provenance.get("adapted_files", []))
    actual = {str(p.relative_to(root)) for p in (root / "skills").rglob("*") if p.is_file()}
    check(actual == set(originals), "Skill inventory differs from the imported release")
    for name, digest in originals.items():
        if name not in adaptations and (root / name).is_file():
            check(hashlib.sha256((root / name).read_bytes()).hexdigest() == digest,
                  f"Undeclared source change: {name}; review and record the adaptation")
    check(adaptations <= actual, "Adaptation refers to a missing source file")
    logo = root / "assets/govtribe-logo.png"
    check(logo.is_file() and logo.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"), "Missing PNG logo")
    if errors:
        raise ValueError("\n".join(errors))
    print(f"Validated {len(skills)} skills, {len(actual)} skill files, manifests, links, Python syntax, and source integrity.")


if __name__ == "__main__":
    try:
        validate()
    except ValueError as error:
        print(error, file=sys.stderr)
        sys.exit(1)
