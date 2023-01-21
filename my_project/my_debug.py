def my_add_numbers(x: int, y: int) -> int:
    return x + y
def my_func(x: str, y: str) -> str:
    """
    숫자 2개를 받아서 3을 더해서 string으로 반환
    """
    return f"{my_add_numbers(x, y) + 3}"

