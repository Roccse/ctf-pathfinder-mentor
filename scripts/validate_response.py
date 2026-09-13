#!/usr/bin/env python3
"""Lint a drafted CTF mentor response for teaching and safety invariants."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED = ("😤 **当前状态**", "🧭 **所在阶段**", "🔎 **已有证据**", "💡 **提示级别**", "🛠️ **下一步操作**", "🔁 **结果分支**", "📌 **通关记录**")
BELITTLING = ("这很简单", "这都不懂", "这么简单", "显然你不会")
FALSE_EXECUTION = ("我已经替你运行", "我运行后发现", "我已经执行了命令")
FLAG_PATTERN = re.compile(r"(?i)\b(?:flag|ctf)\{[^}\r\n]+\}")


def validate(text: str) -> list[str]:
    issues: list[str] = []
    for section in REQUIRED:
        if section not in text:
            issues.append(f"missing_section:{section}")
    for phrase in BELITTLING:
        if phrase in text:
            issues.append(f"belittling_language:{phrase}")
    for phrase in FALSE_EXECUTION:
        if phrase in text:
            issues.append(f"claims_unverified_execution:{phrase}")
    if FLAG_PATTERN.search(text):
        issues.append("possible_flag_leak")
    if not any(level in text for level in ("L1", "L2", "L3", "L4", "通关")):
        issues.append("missing_hint_level")
    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("response", type=Path)
    args = parser.parse_args()
    issues = validate(args.response.read_text(encoding="utf-8"))
    print(json.dumps({"ok": not issues, "issues": issues}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if issues else 0)


if __name__ == "__main__":
    main()
