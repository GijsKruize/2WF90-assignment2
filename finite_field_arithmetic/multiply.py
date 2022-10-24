from polynomial_arithmetic.long_division import long_division
from polynomial_arithmetic.multiply import multiplication as polynomial_multiplication


def multiplication(modulus: int, polynomial_modulus: list[int], f: list[int], g: list[int]):
    result = polynomial_multiplication(modulus, f, g)

    return long_division(modulus, result, polynomial_modulus)
