from typing import TypeVar


def equalize_array_length(f, g):
    new_f = remove_leading_zeros(f)
    new_g = remove_leading_zeros(g)

    f_length = len(new_f)
    g_length = len(new_g)
    max_length = max(f_length, g_length)

    new_f = new_f + [0] * (max_length - f_length)
    new_g = new_g + [0] * (max_length - g_length)

    return new_f, new_g, max_length


def remove_leading_zeros(array):
    rev_array = array[::-1]
    for i in range(len(array)):
        if rev_array[i] != 0:
            rev_array = rev_array[i:]
            return rev_array[::-1]

    if not array:
        return [0]

    return array


T = TypeVar('T')


def remove_duplicates(array):
    return list(dict.fromkeys(array))


def degree(f):
    f = remove_leading_zeros(f)
    return len(f) - 1
