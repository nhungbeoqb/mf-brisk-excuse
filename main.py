#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes the entry line to /output/entry.txt (stdlib only, deterministic).
"""
import os

TEXT = (
    "I didn't miss the deadline \u2014 I finished it in a parallel conversation "
    "I hallucinated at 3 a.m., where you'd already thanked me, "
    "given me five stars, and I'd already felt proud."
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()
