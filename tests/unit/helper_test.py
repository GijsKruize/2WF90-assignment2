from helpers import *


def test_equalize_array_length():
    assert ([1, 2, 3, 4, 0, 0], [1, 2, 1, 2, 3, 4],
            6) == equalize_array_length([1, 2, 3, 4], [1, 2, 1, 2, 3, 4])
    assert ([0] * 6, [1, 2, 1, 2, 3, 4],
            6) == equalize_array_length([], [1, 2, 1, 2, 3, 4])
    assert ([1, 2, 1, 2, 3, 4], [0] * 6,
            6) == equalize_array_length([1, 2, 1, 2, 3, 4], [0])


def test_remove_leading_zeros():
    assert [10, 9, 1, 00, 1, 7] == remove_leading_zeros(
        [10, 9, 1, 00, 1, 7, 0, 0, 0, 0])
    assert [0] == remove_leading_zeros([0])
    assert [0] == remove_leading_zeros([])


def test_remove_duplicates():
    assert [1, 91, 34, 32, 42] == remove_duplicates([1, 1, 91, 34, 32, 42, 42])
    assert [] == remove_duplicates([])
