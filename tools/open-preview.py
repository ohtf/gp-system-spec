# SPDX-FileCopyrightText: 2026 Open Health Technology Foundation contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Open a Zensical preview once its homepage is served."""

import os
import sys
import time
from urllib.request import ProxyHandler, build_opener
import webbrowser


def open_when_ready(url, server_pid):
    # The preview is local. Don't route readiness checks through an HTTP proxy.
    opener = build_opener(ProxyHandler({}))
    deadline = time.monotonic() + 300
    while os.getppid() == server_pid and time.monotonic() < deadline:
        time.sleep(0.5)
        if os.getppid() != server_pid:
            return
        try:
            with opener.open(url, timeout=1) as response:
                if response.status != 200 or not response.read(1):
                    continue
                ready_url = response.url
        except (OSError, ValueError):
            continue
        print(f"s/docs: preview ready at {ready_url}", flush=True)
        if not webbrowser.open(ready_url):
            print("s/docs: could not open a browser; use the URL above", file=sys.stderr)
        return
    if os.getppid() == server_pid:
        print(f"s/docs: preview not ready after 5 minutes; check {url} manually", file=sys.stderr)


if __name__ == "__main__":
    open_when_ready(sys.argv[1], int(sys.argv[2]))
