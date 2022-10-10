import random
from irreducible_check import irreducible_test


def find_irreducible(n, p):
    f = [random.randint(1, p - 1)]
    i = 0

    while i < n - 1:
        f.append(random.randint(0, p - 1))

    irreducible = False

    while not irreducible:
        if irreducible_test(f, p):
            irreducible = True
        else:
            f = [random.randint(1, p - 1)]
            i = 0
            while i < n - 1:
                f.append(random.randint(0, p - 1))

    return f
