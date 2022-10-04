from typing import TypeVar


def equalize_array_length(f: list[int], g: list[int]):
    new_f = remove_leading_zeros(f)
    new_g = remove_leading_zeros(g)

    f_length = len(new_f)
    g_length = len(new_g)
    max_length = max(f_length, g_length)

    new_f = [0] * (max_length - f_length) + new_f
    new_g = [0] * (max_length - g_length) + new_g

    return (new_f, new_g, max_length)


def remove_leading_zeros(array: list[int]):
    for i in range(len(array)):
        if array[i] != 0:
            return array[i:]

    if not array:
        return [0]

    return array


T = TypeVar('T')


def remove_duplicates(array: list[T]):
    return list(dict.fromkeys(array))
