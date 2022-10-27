from polynomial_arithmetic.long_division import long_division
from polynomial_arithmetic.multiply import multiplication
from polynomial_arithmetic.subtract import subtraction


def euclid(modulus: int, f: list[int], g: list[int]):

    a = f
    b = g

    if modulus <= 0:
        return None, None

    r = [a, b]
    x = [[1], [0]]
    y = [[0], [1]]
    i = 1

    while max(r[i]):
        quotient, remainder = long_division(modulus, r[i-1], r[i])
        r.append(remainder)
        x.append(subtraction(modulus, x[i-1], multiplication(modulus, quotient, x[i])))
        y.append(subtraction(modulus, y[i-1], multiplication(modulus, quotient, y[i])))
        i += 1

    gcd = r[i-1]
    a1 = (-1)**(i-1)*y[i]
    b1 = (-1)**i*x[i]

    if not b1:
        b1 = [0]

    return gcd, a1, b1

