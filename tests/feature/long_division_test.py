from tests.feature.assert_answer import assert_exercise


def test_realistic_exercise_1():
    assert_exercise("realistic", 0)


def test_realistic_exercise_2():
    assert_exercise("realistic", 4)


def test_simple_exercise_1():
    assert_exercise("simple", 3)


def test_simple_exercise_2():
    assert_exercise("simple", 4)
