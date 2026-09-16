#!/usr/bin/env python3
"""Build a deterministic, allowlisted plugin ZIP for Claude's upload interface."""

import hashlib
import json
from pathlib import Path
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

sys.dont_write_bytecode = True
from validate import ROOT, validate


def package():
    validate()
    version = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())["version"]
    files = [ROOT / p for p in (".claude-plugin/plugin.json", ".mcp.json", "README.md", "SETUP.md", "LICENSE", "CHANGELOG.md")]
    for directory in ("skills", "assets", "docs"):
        files.extend(p for p in (ROOT / directory).rglob("*") if p.is_file())
    if any(p.is_symlink() for p in files):
        raise ValueError("Refusing to package symlinks")
    total = sum(p.stat().st_size for p in files)
    if len(files) > 5000 or total > 200 * 1024 * 1024:
        raise ValueError("Package exceeds Claude's documented upload limits")
    out = ROOT / "dist"
    out.mkdir(exist_ok=True)
    archive = out / f"govtribe-{version}.zip"
    with ZipFile(archive, "w", ZIP_DEFLATED, compresslevel=9) as bundle:
        for path in sorted(files):
            info = ZipInfo(path.relative_to(ROOT).as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = ZIP_DEFLATED
            bundle.writestr(info, path.read_bytes(), compresslevel=9)
    with ZipFile(archive) as bundle:
        if bundle.testzip() is not None:
            raise ValueError("ZIP integrity check failed")
        assert ".claude-plugin/plugin.json" in bundle.namelist()
        assert ".mcp.json" in bundle.namelist()
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (out / "SHA256SUMS").write_text(f"{digest}  {archive.name}\n")
    print(f"Built {archive.name}: {len(files)} files, {total:,} bytes uncompressed, SHA256 {digest}")
    return archive


if __name__ == "__main__":
    package()
