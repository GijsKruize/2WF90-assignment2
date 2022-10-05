from helpers import degree, equalize_array_length, remove_leading_zeros


def long_division(mod, f, g):
    # First we check if polynomial g is not 0 and the modulus is not 0
    if ((mod == 0) | (g == [0])):
        return ([], [])  # this will be our error state

    # If the denominator is bigger than the numerator, it will return the numerator as the remainder
    if len(remove_leading_zeros(f)) >= len(remove_leading_zeros(g)):
        f, g, _ = equalize_array_length(f, g)
    else:
        return (0, f)

    dG = degree(g)
    dF = degree(f)

    if dG < 0:
        raise ZeroDivisionError

    if dF >= dG:
        q = [0] * dF

        while dF >= dG:
            d = [0] * (dF - dG) + g
            mult = q[dF - dG] = f[-1] / float(d[-1])
            d = [coeff * mult for coeff in d]
            f = [coeffN - coeffd for coeffN, coeffd in zip(g, d)]
            dF = degree(f)

        r = f

    return q, r
