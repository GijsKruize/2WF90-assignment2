
from helpers import equalize_array_length, get_leading_coefficent, reduction, remove_leading_zeros, get_degree
from polynomial_arithmetic.subtract import subtraction
from polynomial_arithmetic.multiply import multiplication


def long_division(modulus: int, f: list[int], g: list[int]):
    if modulus <= 0:
        return None, None
    if remove_leading_zeros(g) == [0]:
        return None, None

    f, g, max_length = equalize_array_length(f, g)

    q = max_length * [0]
    r = f

    while get_degree(g) <= get_degree(r):
        leading_r_coefficient = get_leading_coefficent(r)
        leading_coefficient = leading_r_coefficient / get_leading_coefficent(g)

        while leading_coefficient != int(leading_coefficient):
            leading_r_coefficient += modulus

            leading_coefficient = leading_r_coefficient / \
                get_leading_coefficent(g)

        leading_coefficient = int(leading_coefficient)
        degree = get_degree(r) - get_degree(g)

        q[degree] = leading_coefficient

        result = multiplication(
            modulus, [0] * degree + [leading_coefficient], g)
        r = subtraction(modulus, r, result)
        r = reduction(modulus, r)

    return remove_leading_zeros(q), remove_leading_zeros(r)
