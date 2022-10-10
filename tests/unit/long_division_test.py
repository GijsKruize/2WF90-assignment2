from polynomial_arithmetic.long_division import long_division


def test_lecture_example():
    f = [6, 1, 10]
    g = [1, 2]
    assert [97, 5], [8] == long_division(99, f, g)
