"""Unpack only the verified website runtime, without exposing tests or recovery files."""
from __future__ import annotations

import hashlib
import shutil
import stat
import tempfile
from pathlib import Path, PurePosixPath
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / "AI_for_science_workshop_v4.zip"
EXPECTED_SHA256 = "4b3d767f823721d7693518b0fe23c216f52dde62580ea67d00f9f28e460d5e86"
PREFIX = "ai_science_workshop_v4/"
REQUIRED = {
    "room_app.py", "room_decks.py", "requirements.txt",
    "public/index.html", "public/room/index.html", "public/room/template.pptx",
}
TOP_LEVEL = {"room_app.py", "room_decks.py", "requirements.txt", "README.md"}


def prepare() -> Path:
    if not ARCHIVE.is_file():
        raise SystemExit(
            "Missing AI_for_science_workshop_v4.zip. Upload the original, unchanged "
            "workshop ZIP to the repository root before deploying. See deploy/README.md."
        )
    if ARCHIVE.stat().st_size > 32 * 1024 * 1024:
        raise SystemExit("The workshop archive exceeds the expected size limit.")
    digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit("Workshop ZIP checksum mismatch. Use the original v4 archive.")
    destination = ROOT / "website"
    with tempfile.TemporaryDirectory(prefix=".workshop-build-", dir=ROOT) as tmp:
        staging = Path(tmp)
        seen: set[str] = set()
        total = 0
        with ZipFile(ARCHIVE) as package:
            for entry in package.infolist():
                if entry.is_dir() or not entry.filename.startswith(PREFIX):
                    continue
                relative = entry.filename[len(PREFIX):]
                if relative not in TOP_LEVEL and not relative.startswith("public/"):
                    continue
                path = PurePosixPath(relative)
                if path.is_absolute() or ".." in path.parts or "\\" in relative:
                    raise SystemExit("Unsafe path in workshop archive.")
                if stat.S_ISLNK(entry.external_attr >> 16) or relative in seen:
                    raise SystemExit("Symlink or duplicate path in workshop archive.")
                total += entry.file_size
                if total > 32 * 1024 * 1024:
                    raise SystemExit("Expanded runtime exceeds its size limit.")
                output = staging.joinpath(*path.parts)
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_bytes(package.read(entry))
                seen.add(relative)
        if REQUIRED - seen:
            raise SystemExit("The archive is missing required website runtime files.")
        if destination.is_symlink():
            raise SystemExit("Refusing to replace a symlink at website/.")
        if destination.exists():
            shutil.rmtree(destination)
        staging.rename(destination)
    from fix_layout_ids import apply
    apply(destination)
    print(f"Verified and prepared {len(seen)} runtime files; applied unique layout-ID merger fix.")
    return destination


if __name__ == "__main__":
    prepare()
