from polynomial_arithmetic.long_division import long_division
from polynomial_arithmetic.multiply import multiplication as polynomial_multiplication


def multiplication(modulus, polynomial_modulus, f, g):
    result = polynomial_multiplication(modulus, f, g)

    return long_division(modulus, polynomial_modulus, result)[0]
