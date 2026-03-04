"""
简单的计算器模块，用于测试 porygon_t
"""


def add(a: float, b: float) -> float:
    """加法运算"""
    return a + b


def subtract(a: float, b: float) -> float:
    """减法运算"""
    return a - b


def multiply(a: float, b: float) -> float:
    """乘法运算"""
    return a * b


def divide(a: float, b: float) -> float:
    """除法运算，除数为0时抛出异常"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b


def power(base: float, exponent: float) -> float:
    """幂运算"""
    return base ** exponent


class Calculator:
    """计算器类，支持链式调用"""

    def __init__(self, initial_value: float = 0):
        self.value = initial_value

    def add(self, n: float) -> 'Calculator':
        self.value += n
        return self

    def subtract(self, n: float) -> 'Calculator':
        self.value -= n
        return self

    def multiply(self, n: float) -> 'Calculator':
        self.value *= n
        return self

    def divide(self, n: float) -> 'Calculator':
        if n == 0:
            raise ValueError("除数不能为零")
        self.value /= n
        return self

    def clear(self) -> 'Calculator':
        self.value = 0
        return self

    def get_result(self) -> float:
        return self.value
