from tests.feature.assert_answer import assert_exercise


def test_realistic_exercise_1():
    assert_exercise("realistic", 5)


def test_realistic_exercise_2():
    assert_exercise("realistic", 17)


def test_simple_exercise_1():
    assert_exercise("simple", 5)


def test_simple_exercise_2():
    assert_exercise("simple", 6)
