"""Optional maintainer checks. ADAC users need only the Markdown release."""
import argparse
import re
from pathlib import Path
from urllib.parse import unquote

RELEASE = "2.3.0"
RECOMMENDATIONS = "1.2.0"
# Generic patterns, not an inventory of anyone's private infrastructure.
PRIVATE = re.compile(r"(?:/home/|/Users/)[A-Za-z][^\s\"')]*|(?:https?://|ssh://)[^\s/]*\.home\b|\b(?:10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+|172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+)\b")
SECRET = re.compile(r"-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----|\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b|\bsk-[A-Za-z0-9]{32,}\b")


def public_files(root):
    return (root / "maintainer/public-files.txt").read_text().splitlines()


def without_fences(text):
    return re.sub(r"(?ms)^\s*```.*?^\s*```[^\n]*$", "", text)


def anchors(text):
    seen = {}
    result = set()
    for title in re.findall(r"(?m)^#{1,6} (.+)$", without_fences(text)):
        title = re.sub(r"[^\w\- ]", "", title.lower()).strip().replace(" ", "-")
        count = seen.get(title, 0)
        seen[title] = count + 1
        result.add(title if count == 0 else title + "-" + str(count))
    return result


def check(root):
    errors = []
    names = public_files(root)
    if len(names) != len(set(names)):
        errors.append("duplicate public path")
    allowed = set(names)
    for name in names:
        rel = Path(name)
        if rel.is_absolute() or ".." in rel.parts:
            errors.append("unsafe manifest path: " + name)
            continue
        path = root / rel
        if not path.is_file() or path.is_symlink():
            errors.append("missing or symbolic public file: " + name)
            continue
        if path.suffix.lower() == ".png":
            # Raster appearance and metadata require manual publication review.
            if not path.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"):
                errors.append("invalid PNG signature: " + name)
            continue
        text = path.read_text(encoding="utf-8")
        if PRIVATE.search(text) or SECRET.search(text):
            errors.append("private reference or potential secret: " + name)
        if path.suffix != ".md":
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", without_fences(text)):
            target = target.split(' "', 1)[0].strip("<>")
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            filepart, _, anchor = target.partition("#")
            dest = (path.parent / unquote(filepart)).resolve() if filepart else path.resolve()
            try:
                relative = dest.relative_to(root.resolve()).as_posix()
            except ValueError:
                errors.append("link escapes package: " + name)
                continue
            if relative not in allowed or not dest.is_file():
                errors.append("broken/local-unbundled link: " + name + " -> " + target)
            elif anchor and unquote(anchor) not in anchors(dest.read_text()):
                errors.append("broken anchor: " + name + " -> " + target)
    expectations = {
        "releases/"+RELEASE+"/core.md": "# ADAC core "+RELEASE,
        "releases/"+RELEASE+"/recommendations.md": "# Task and capability recommendations "+RECOMMENDATIONS,
        "releases/"+RELEASE+"/README.md": "# ADAC "+RELEASE,
    }
    for name, heading in expectations.items():
        path=root/name
        if not path.is_file() or not path.read_text().startswith(heading):
            errors.append("version mismatch: " + name)
    for name in ["README.md", "AGENTS.md"]:
        path=root/name
        if path.is_file() and "releases/"+RELEASE+"/" not in path.read_text():
            errors.append("current release pointer missing: " + name)
    return errors


if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    args=parser.parse_args()
    errors=check(args.root)
    for error in errors: print(error)
    print("Public file checks:", "FAIL" if errors else "PASS")
    raise SystemExit(bool(errors))
