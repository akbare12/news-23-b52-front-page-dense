#!/usr/bin/env python3
"""news-23 b52 front-page-dense: copy entry.png (1024x1024) to $MAKEFUN_OUTPUT_DIR/entry.png.

Stdlib only. Never writes next to itself: it writes only to MAKEFUN_OUTPUT_DIR,
so it also works from a read-only copy (with MAKEFUN_OUTPUT_DIR pointed elsewhere).
"""
import hashlib
import os
import struct
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
MAX_BYTES = 1024 * 1024


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is empty", file=sys.stderr)
        return 1
    repo = os.path.dirname(os.path.abspath(__file__))
    if os.path.abspath(out_dir) == repo or os.path.abspath(out_dir).startswith(repo + os.sep):
        print("error: MAKEFUN_OUTPUT_DIR must not be inside the repo", file=sys.stderr)
        return 1
    if not os.path.exists(SRC):
        print("error: entry.png missing next to main.py", file=sys.stderr)
        return 1
    with open(SRC, "rb") as f:
        data = f.read()
    if len(data) > MAX_BYTES:
        print("error: entry.png is %d bytes, over 1 MiB" % len(data), file=sys.stderr)
        return 1
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("error: entry.png is not a PNG", file=sys.stderr)
        return 1
    w, h, depth, ctype = struct.unpack(">IIBB", data[16:26])
    if (w, h) != (1024, 1024) or depth != 8 or ctype not in (2, 6):
        print("error: bad IHDR %dx%d depth %d colour %d" % (w, h, depth, ctype), file=sys.stderr)
        return 1
    if data[-12:] != b"\x00\x00\x00\x00IEND\xaeB`\x82":
        print("error: PNG trailer (IEND) is not well-formed", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(dst, "wb") as f:
        f.write(data)
    with open(dst, "rb") as f:
        back = f.read()
    if back != data:
        print("error: output does not match source", file=sys.stderr)
        return 1
    print("ok: wrote %s (%d bytes, %dx%d, sha256 %s)" % (dst, len(data), w, h, hashlib.sha256(data).hexdigest()))
    print("source: %d bytes, sha256 %s" % (len(data), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
