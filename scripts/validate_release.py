import json
import pathlib
import re
import subprocess

root = pathlib.Path(__file__).resolve().parents[1]
manifest = json.loads((root / "release-info.json").read_text(encoding="utf-8"))
assert manifest["name"] == "Idle Sryfe Miner"
assert manifest["applicationId"] == "win.fantest.idlesryfeminer"
assert re.fullmatch(r"CP[0-9]{3}", manifest["checkpoint"])
assert re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", manifest["version"])
assert manifest["privateSource"] is True
assert manifest["monetizationEnabled"] is False
assert isinstance(manifest["published"], bool)
assert manifest["downloadUrl"] is None or str(manifest["downloadUrl"]).startswith("https://")
allowed = {
    "README.md", "release-info.json", ".gitignore",
    ".github/workflows/public-metadata.yml", "scripts/validate_release.py",
}
tracked = subprocess.check_output(["git", "ls-files"], cwd=root, text=True).splitlines()
unexpected = set(tracked) - allowed
assert not unexpected, f"Disallowed files in public CI repository: {sorted(unexpected)}"
assert set(tracked) == allowed, "Public release infrastructure missing required files"
print("Public manifest valid; source leakage guard passed.")
