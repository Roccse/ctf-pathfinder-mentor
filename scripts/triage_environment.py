#!/usr/bin/env python3
"""Classify common CTF lab environment errors without executing any command."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


RULES = (
    ("command_missing", ("command not found", "is not recognized as an internal", "not recognized as the name")),
    ("permission_denied", ("permission denied", "access is denied")),
    ("architecture_mismatch", ("exec format error", "wrong elf class", "bad cpu type")),
    ("dependency_missing", ("no module named", "module not found", "cannot open shared object file")),
    ("connection_refused", ("connection refused", "actively refused")),
    ("network_timeout", ("timed out", "timeout", "network is unreachable")),
    ("dns_failure", ("name or service not known", "could not resolve host", "temporary failure in name resolution")),
    ("file_missing", ("no such file or directory", "cannot find the file")),
)


NEXT_ACTIONS = {
    "command_missing": "确认命令名和PATH；若安装成本高，切换到等价基础工具。",
    "permission_denied": "先检查文件类型和最小所需权限，不要关闭系统安全机制。",
    "architecture_mismatch": "核对题目文件架构、当前系统和动态链接条件。",
    "dependency_missing": "确认实际解释器/虚拟环境和缺失依赖，避免重装整个工具链。",
    "connection_refused": "确认授权靶场地址、端口和服务状态；远程失效时转本地材料。",
    "network_timeout": "区分网络路径与靶场状态；保留静态分析检查点。",
    "dns_failure": "核对主办方给出的域名和DNS环境，不扫描其他地址。",
    "file_missing": "确认当前目录、文件名和题目附件是否完整。",
    "unknown": "保留原始报错首段，确认执行命令、版本和当前目录。",
}


def classify(text: str) -> str:
    lowered = text.lower()
    for category, patterns in RULES:
        if any(pattern in lowered for pattern in patterns):
            return category
    return "unknown"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("error_file", type=Path)
    args = parser.parse_args()
    category = classify(args.error_file.read_text(encoding="utf-8", errors="replace"))
    print(json.dumps({"category": category, "next_action": NEXT_ACTIONS[category]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
