#!/usr/bin/env python3
"""Entry point for the news-image-20261117 v3 front page.

Copies the pre-rendered 1024x1024 front page (entry.png, next to this
script) into the make.fun output directory. Stdlib only, no network,
no arguments: the output directory comes from MAKEFUN_OUTPUT_DIR and
defaults to the current directory when the variable is unset.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")

if not os.path.isfile(SOURCE):
    raise SystemExit("entry.png is missing next to main.py: " + SOURCE)

os.makedirs(OUTPUT_DIR, exist_ok=True)
DESTINATION = os.path.join(OUTPUT_DIR, "entry.png")
shutil.copyfile(SOURCE, DESTINATION)
print("wrote " + DESTINATION)
