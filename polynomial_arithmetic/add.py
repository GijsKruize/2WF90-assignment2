from helpers import equalize_array_length


def addition(modulus: int, f: list[int], g: list[int]):
    if (modulus <= 0):
        return None

    f, g, max_length = equalize_array_length(f, g)

    result = [0] * max_length

    for i in range(max_length):
        result[i] = (f[i] + g[i]) % modulus

    return result
