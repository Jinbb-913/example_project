"""
字符串处理工具模块，用于测试 porygon_t
"""

import re
from typing import List, Optional


def reverse_string(s: str) -> str:
    """反转字符串"""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """判断是否为回文字符串（忽略大小写和非字母数字字符）"""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]


def count_words(s: str) -> int:
    """统计单词数量"""
    if not s.strip():
        return 0
    return len(s.split())


def truncate_string(s: str, max_length: int, suffix: str = "...") -> str:
    """截断字符串到指定长度"""
    if max_length <= 0:
        raise ValueError("max_length 必须大于0")
    if len(s) <= max_length:
        return s
    return s[:max_length - len(suffix)] + suffix


def find_duplicates(strings: List[str]) -> List[str]:
    """找出列表中重复的字符串"""
    seen = set()
    duplicates = set()
    for s in strings:
        if s in seen:
            duplicates.add(s)
        seen.add(s)
    return list(duplicates)


class TextFormatter:
    """文本格式化工具类"""

    def __init__(self, indent_size: int = 4):
        self.indent_size = indent_size

    def indent(self, text: str, level: int = 1) -> str:
        """为文本添加缩进"""
        if level < 0:
            raise ValueError("缩进级别不能为负数")
        prefix = " " * (self.indent_size * level)
        return prefix + text

    def format_list(self, items: List[str], bullet: str = "-") -> str:
        """格式化列表为带项目符号的文本"""
        return "\n".join(f"{bullet} {item}" for item in items)

    def wrap_text(self, text: str, width: int) -> List[str]:
        """将文本按指定宽度换行"""
        if width <= 0:
            raise ValueError("宽度必须大于0")

        words = text.split()
        if not words:
            return []

        lines = []
        current_line = [words[0]]
        current_length = len(words[0])

        for word in words[1:]:
            if current_length + 1 + len(word) <= width:
                current_line.append(word)
                current_length += 1 + len(word)
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_length = len(word)

        if current_line:
            lines.append(" ".join(current_line))

        return lines
