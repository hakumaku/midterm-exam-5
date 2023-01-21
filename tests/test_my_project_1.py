from my_project.my_utils import my_add_numbers


def test_my_add_numbers_should_return_10():
    x = 1
    y = 2
    actual = my_add_numbers(x, y)
    expected = 7
    assert actual == expected
