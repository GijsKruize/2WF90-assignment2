from helpers import equalize_array_length, remove_leading_zeros


def subtraction(modulus: int, f: list[int], g: list[int]):
    if modulus <= 0:
        return None

    f, g, max_length = equalize_array_length(f, g)

    result = []

    for i in range(max_length):
        result.append((f[i] - g[i]) % modulus)

    return remove_leading_zeros(result)
