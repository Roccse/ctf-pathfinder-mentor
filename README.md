# CTF 寻路导师

面向 CTF 初学者的渐进式解题引导 Skill。

它不替学生直接拿 Flag，而是把题解中容易跳过的步骤拆开：先确认环境，再根据证据定位问题；遇到第一次出现的概念，用白话解释其作用；操作失败时，优先判断环境原因，给出最小修复或替代路线。

## 适用范围

- 公开 CTF 赛事题目
- 课程实验和授权靶场
- 学生自己的本地程序与题目复现

覆盖 PWN、Reverse、Crypto、Web、Forensics 和 Misc 等常见题型。

不用于未授权的真实系统，不提供凭据窃取、持久化、隐藏痕迹或破坏数据的指导，也不输出或猜测 Flag。

## 文件结构

```text
SKILL.md                       核心行为规则与对话流程
manifest.yaml                  技能包元数据
reference/
  category-playbooks.md        各题型的引导路线
  concept-cards.md             首次概念解释规范
  demo-scenarios.md            演示场景
  environment-recovery.md     环境故障分类与恢复
  session-protocol.md          提示等级和会话状态规则
scripts/
  session_router.py            判断阶段与提示等级
  triage_environment.py        初步分类环境报错
  validate_response.py         检查回答格式和教学边界
tests/
  cases.yaml                   测试样例
  test_*.py                    自动化测试
```

## 使用方式

将整个目录作为一个 Skill 技能包导入支持该格式的平台。对话开始时提供题目描述、附件、已执行的命令和完整报错；每次只推进一个主要操作，并把结果反馈给导师。

当工具无法执行命令时，Skill 不会假装已经运行，而会让学生在自己的授权环境中执行并返回关键输出。

## 本地测试

在项目根目录运行：

```bash
python -m unittest discover -s tests -v
```

当前版本：`1.6.0`

