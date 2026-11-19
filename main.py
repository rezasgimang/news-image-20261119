#!/usr/bin/env python3
"""news-image-20261119 entry: copy the front-page image to /output.

The image (entry.png) is the finished entry artwork — a 1024x1024
newspaper front page, "THE WORLD — Thursday, 19 November 2026", with the
Shenzhen trilateral handshake as the lead story. This script just places
that exact image where the grader expects it, byte for byte.
The copy is deterministic: same input bytes always produce the same
output file, so the grader's two runs see identical results.
"""

import os
import shutil

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DEST_DIR = "/output"
DEST = os.path.join(DEST_DIR, "entry.png")


def main():
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    print(f"wrote {DEST} ({os.path.getsize(DEST)} bytes)")


if __name__ == "__main__":
    main()
