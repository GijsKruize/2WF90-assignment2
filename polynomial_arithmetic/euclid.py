from polynomial_arithmetic.long_division import long_division
from polynomial_arithmetic.multiply import multiplication
from polynomial_arithmetic.subtract import subtraction


def euclid(modulus: int, f: list[int], g: list[int]):

    a = f
    b = g

    if modulus <= 0:
        return None, None

    x1 = [1]
    x2 = [0]
    y1 = [0]
    y2 = [1]

    while max(b) > 0:
        quotient, r = long_division(modulus, a, b)
        a = b
        b = r
        x3 = subtraction(modulus, x1, multiplication(modulus, quotient, x2))
        y3 = subtraction(modulus, y1, multiplication(modulus, quotient, y2))
        x1 = x2
        y1 = y2
        x2 = x3
        y2 = y3

    return a, x1, y1

