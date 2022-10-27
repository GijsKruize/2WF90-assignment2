import random
from polynomial_arithmetic.irredCheck import irreducibleTest


def find_irreducible(n, p):
    f = [random.randint(0, p - 1)]
    i = 0

    while i < n-1:
        f.append(random.randint(0, p - 1))
        i=i+1

    irreducible = False
    f.append(random.randint(1, p - 1))

    while not irreducible:
        if irreducibleTest(p, f):
            irreducible = True
        else:
            f = [random.randint(0, p - 1)]
            i = 0
            while i < n-1:
                f.append(random.randint(0, p - 1))
                i = i + 1
            f.append(random.randint(1, p - 1))
    return f
