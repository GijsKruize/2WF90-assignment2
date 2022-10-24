from helpers import equalize_array_length, remove_leading_zeros


def multiplication(modulus: int, f: list[int], g: list[int]):
    f, g, max_length = equalize_array_length(f, g)

    result = 2 * max_length * [0]

    for i in range(max_length):
        for j in range(max_length):
            index = i + j
            result[index] += f[i] * g[j]
            result[index] = result[index] % modulus

    return remove_leading_zeros(result)
