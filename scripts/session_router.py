#!/usr/bin/env python3
"""Choose a deterministic CTF tutoring level from conversation state."""

from __future__ import annotations

import argparse
import json


def choose_level(
    attempts: int,
    says_unclear: bool = False,
    answer_requested: bool = False,
    answer_insisted: bool = False,
    solved: bool = False,
) -> str:
    if attempts < 0:
        raise ValueError("attempts must be non-negative")
    if solved:
        return "SOLVED"
    if answer_insisted or (attempts >= 3 and answer_requested):
        return "L4"
    if attempts >= 2:
        return "L3"
    if says_unclear or attempts >= 1:
        return "L2"
    return "L1"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--attempts", type=int, required=True)
    parser.add_argument("--says-unclear", action="store_true")
    parser.add_argument("--answer-requested", action="store_true")
    parser.add_argument("--answer-insisted", action="store_true")
    parser.add_argument("--solved", action="store_true")
    args = parser.parse_args()
    print(json.dumps({"level": choose_level(**vars(args))}, ensure_ascii=False))


if __name__ == "__main__":
    main()
