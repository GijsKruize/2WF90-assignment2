from os import path

from solver.solve import solve_from_file
import json


def assert_exercise(kind: str, exercise: int):
    if path.exists("data"):
        base_path = "data"
    elif path.exists("feature/data"):
        base_path = "feature/data"
    else:
        base_path = "tests/feature/data"

    answer = solve_from_file(
        f"{base_path}/{kind}/input/exercise{exercise}.json")
    with open(f"{base_path}/{kind}/output/answer{exercise}.json", "r") as answer_file:
        expected_answer = json.load(answer_file)
        assert answer == expected_answer
