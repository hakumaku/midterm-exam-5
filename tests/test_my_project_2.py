import pytest
from my_project.my_complex import my_complex_add_numbers


@pytest.mark.parametrize("arguments,expected", [((1, 2, 3, 4), 10)])
def test_my_add_complex_numbers(arguments, expected):
    x, y, z, v = arguments
    actual = my_complex_add_numbers(x, y, z, v)
    assert actual == expected
