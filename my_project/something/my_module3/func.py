import math


def my_func1(a: int) -> str:
    return f"a: {a}"


def my_func2(a: int) -> int:
    _ = my_func1(a)
    return 1
