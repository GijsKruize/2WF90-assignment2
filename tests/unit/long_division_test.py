from polynomial_arithmetic.long_division import long_division


def test_lecture_example():
    f = [6, 1, 10]
    g = [1, 2]
    assert [97, 5], [8] == long_division(99, f, g)


def test_zero_division():
    f = [6, 1, 10]
    g = [1, 2]
    print(long_division(99, [0], [23]))
    assert ([0], [0]) == long_division(9, [0], [0])
