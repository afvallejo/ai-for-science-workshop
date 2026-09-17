"""Run the saved workshop on Render and initialise one non-sensitive test room."""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "website"


def create_app():
    mount = os.environ.get("WORKSHOP_REQUIRE_MOUNT", "")
    if mount and not os.path.ismount(mount):
        raise RuntimeError("Persistent disk is not mounted. Refusing temporary slide storage.")
    storage = os.environ.get("WORKSHOP_DATA", "")
    if not storage:
        raise RuntimeError("Set WORKSHOP_DATA to the private persistent storage directory.")
    data_path = Path(storage).resolve()
    if mount and not data_path.is_relative_to(Path(mount).resolve()):
        raise RuntimeError("WORKSHOP_DATA must be inside the persistent disk.")
    if data_path.is_relative_to(SITE.resolve()):
        raise RuntimeError("Private room data must not be stored inside the website runtime.")
    host_key = os.environ.get("WORKSHOP_HOST_KEY", "")
    if len(host_key) < 32:
        raise RuntimeError("WORKSHOP_HOST_KEY must contain at least 32 random characters.")
    if not (SITE / "public" / "room" / "index.html").is_file():
        raise RuntimeError("Website runtime is missing. Run deploy/prepare_workshop.py first.")
    sys.path.insert(0, str(SITE))
    import room_app

    if os.environ.get("WORKSHOP_CREATE_TEST_ROOM", "").lower() == "true":
        code = os.environ.get("WORKSHOP_TEST_ROOM_CODE", "SCITEST2")
        token = os.environ.get("WORKSHOP_TEST_ROOM_KEY", "")
        if not re.fullmatch(r"[A-Z2-9]{8}", code):
            raise RuntimeError("The test room code must contain eight valid characters.")
        if len(token) < 32 or token == host_key:
            raise RuntimeError("Use a separate random WORKSHOP_TEST_ROOM_KEY of 32+ characters.")
        with room_app.db() as connection:
            connection.execute("BEGIN IMMEDIATE")
            connection.execute(
                "CREATE TABLE IF NOT EXISTS deployment_initialisation "
                "(name TEXT PRIMARY KEY, room_code TEXT NOT NULL)"
            )
            existing = connection.execute(
                "SELECT room_code FROM deployment_initialisation WHERE name='test_room_v1'"
            ).fetchone()
            if existing is None:
                collision = connection.execute("SELECT 1 FROM rooms WHERE code=?", (code,)).fetchone()
                if collision:
                    raise RuntimeError("Test room code already belongs to another room.")
                connection.execute(
                    "INSERT INTO rooms (code,title,owner_hash,created) VALUES (?,?,?,?)",
                    (code, "AI for science, test room", room_app.digest(token), room_app.now()),
                )
                connection.execute(
                    "INSERT INTO deployment_initialisation (name,room_code) VALUES (?,?)",
                    ("test_room_v1", code),
                )
                print(f"Initialised test room {code}. Management credentials are not logged.", flush=True)
            else:
                # Do not recreate a deleted room or overwrite its settings on a restart.
                if existing["room_code"] != code:
                    raise RuntimeError("Test room code changed. Restore its original environment value.")
                room = connection.execute("SELECT owner_hash FROM rooms WHERE code=?", (code,)).fetchone()
                if room and room["owner_hash"] != room_app.digest(token):
                    raise RuntimeError("Test room key changed. Restore its original environment value.")
    return room_app.app


if __name__ == "__main__":
    import uvicorn

    app = create_app()
    port = int(os.environ.get("PORT", "10000"))
    if not 1 <= port <= 65535:
        raise RuntimeError("PORT is outside the valid range.")
    # Render's edge terminates HTTPS. Forwarded scheme information is required by
    # the original application's same-origin write protection.
    uvicorn.run(
        app, host="0.0.0.0", port=port, workers=1,
        proxy_headers=True, forwarded_allow_ips="*",
        server_header=False,
    )
