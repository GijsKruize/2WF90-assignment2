from helpers import equalize_array_length, remove_leading_zeros


def multiplication(modulus, f, g):
    f, g, max_length = equalize_array_length(f, g)

    # TODO rewrite
    result_length = (2 * len(f)) - 1
    result = [0] * result_length

    for i in range(max_length):
        for j in range(max_length):
            result[i + j] += f[i] * g[j]
            result[i + j] = result[i + j] % modulus

    return remove_leading_zeros(result)
