from os import path

from solver.solve import solve_from_file
import json


def assert_exercise(kind: str, exercise: int):
    if path.exists(f"data/{kind}/input/exercise{exercise}.json"):
        answer = solve_from_file(
            f"data/{kind}/input/exercise{exercise}.json")
        with open(f"data/{kind}/output/answer{exercise}.json", "r") as answer_file:
            expected_answer = json.load(answer_file)
            assert answer == expected_answer
    elif path.exists(f"tests/feature/data/{kind}/input/exercise{exercise}.json"):
        with open(f"tests/feature/data/{kind}/output/answer{exercise}.json", "r") as answer_file:
            answer = solve_from_file(
                f"tests/feature/data/{kind}/input/exercise{exercise}.json")
            expected_answer = json.load(answer_file)
            assert answer == expected_answer
    elif path.exists(f"feature/data/{kind}/input/exercise{exercise}.json"):
        with open(f"feature/data/{kind}/output/answer{exercise}.json", "r") as answer_file:
            answer = solve_from_file(
                f"feature/data/{kind}/input/exercise{exercise}.json")
            expected_answer = json.load(answer_file)
            assert answer == expected_answer
