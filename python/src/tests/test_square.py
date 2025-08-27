import pytest


def square(n: int) -> int:
    """
    计算一个数的平方
    :param n: 输入的数
    :return: 输入数的平方
    """
    return n ** 2

@pytest.mark.parametrize("n, expected", [
    (2, 4),
    (3, 9),
    (0, 0),
])
def test_square(n, expected):
    assert square(n) == expected


