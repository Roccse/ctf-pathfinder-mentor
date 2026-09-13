import unittest

from scripts.validate_response import validate


VALID = """😤 **当前状态**：已拿到第一条线索。
🧭 **所在阶段**：PWN｜环境检查｜尚无保护信息。
🔎 **已有证据**：文件来自本地课程题。
💡 **提示级别**：L1。
🛠️ **下一步操作**：查看文件类型。
🔁 **结果分支**：根据32位或64位选择后续工具；失败时贴原始报错。
📌 **通关记录**：有效尝试0次。
"""


class ResponseValidatorTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate(VALID), [])

    def test_flag_leak(self):
        self.assertIn("possible_flag_leak", validate(VALID + "flag{secret}"))

    def test_missing_section(self):
        issues = validate(VALID.replace("📌 **通关记录**", "记录"))
        self.assertTrue(any(item.startswith("missing_section") for item in issues))

    def test_false_execution(self):
        self.assertIn("claims_unverified_execution:我已经替你运行", validate(VALID + "我已经替你运行"))

    def test_belittling(self):
        self.assertIn("belittling_language:这很简单", validate(VALID + "这很简单"))


if __name__ == "__main__":
    unittest.main()
