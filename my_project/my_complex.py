def my_complex_add_numbers(x: int, y: int, z: int, v: int) -> int:
    if x == 10:
        x = 1

    if x == 5 and y == 3:
        x = 1
        y = 2

    if x == 7 or y == 4:
        if z == 1:
            z = 0
        elif v == 1:
            v = 0
        x = 1
        y = 2

    return x + y + z + v
