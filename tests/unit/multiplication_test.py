from polynomial_arithmetic.multiply import multiplication


def test_multiplication_with_leading():
    f = [5, 0]
    g = [1, 2, 0]

    assert [4, 0, 18, 2, 18, 6] == multiplication(99, [4, 0, 6, 2], [1, 0, 3])
    assert [1, 4, 4] == multiplication(99, [1, 2], [1, 2])
    assert [5, 10] == multiplication(99, f, g)
