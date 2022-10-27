##
# 2WF90 Algebra for Security -- Software Assignment 2
# Polynomial and Finite Field Arithmetic
# solve.py
#
#
# Group number:
# 7
#
# Author names and student IDs:
# Gijs Kruize (1658662)
# Christian Groothuis (1715534)
# Jordy Verhoeven (1001249)
# Niels Boonstra (1451294)
##
import json
from finite_field_arithmetic.primitive_check import primitive_check

from polynomial_arithmetic.add import addition
from polynomial_arithmetic.euclid import euclid
from polynomial_arithmetic.long_division import long_division
from polynomial_arithmetic.multiply import multiplication as polynomial_multiplication
from finite_field_arithmetic.multiply import multiplication as finite_field_multiplication
from polynomial_arithmetic.subtract import subtraction
from polynomial_arithmetic.euclid import euclid
from polynomial_arithmetic.irredCheck import irreducibleTest
from polynomial_arithmetic.Generator import find_irreducible

def solve(exercise: object):
    exercise_type = exercise["type"]
    exercise_task = exercise["task"]
    integer_modulus = exercise["integer_modulus"]


    if integer_modulus <= 0:
        return {"answer": None}

    if exercise_type == "polynomial_arithmetic":
        if exercise_task == "addition":
            return {"answer": addition(integer_modulus, exercise["f"], exercise["g"])}

        elif exercise_task == "subtraction":
            return {"answer": subtraction(integer_modulus, exercise["f"], exercise["g"])}

        elif exercise_task == "multiplication":
            return {"answer": polynomial_multiplication(integer_modulus, exercise["f"], exercise["g"])}

        elif exercise_task == "long_division":
            q, r = long_division(integer_modulus, exercise["f"], exercise["g"])
            return {"answer-q": q, "answer-r": r}

        elif exercise_task == "extended_euclidean_algorithm":
            a, b, gcd = euclid(integer_modulus, exercise["f"], exercise["g"])
            return {"answer-a": a, "answer-b": b, "answer-gcd": gcd}

        elif exercise_task == "irreducibility_check":
            return {"answer": irreducibleTest(integer_modulus, exercise["f"])}

        elif exercise_task == "extended_euclidean_algorithm":
            q, r, a = euclid(integer_modulus, exercise["f"], exercise["g"])
            return {"answer-a": q, "answer-b": r, "answer-gcd": a}

        elif exercise_task == "irreducible_element_generation":
            return {"answer": find_irreducible(integer_modulus,exercise["degree"])}

    elif exercise_type == "finite_field_arithmetic":
        polynomial_modulus = exercise["polynomial_modulus"]

        if exercise_task == "addition":
            return {"answer": addition(integer_modulus, exercise["f"], exercise["g"])}

        elif exercise_task == "subtraction":
            return {"answer": subtraction(integer_modulus, exercise["f"], exercise["g"])}

        elif exercise_task == "multiplication":
            return {"answer": finite_field_multiplication(integer_modulus, polynomial_modulus, exercise["f"], exercise["g"])[1]}

        elif exercise_task == "primitivity_check":
            return {"answer" : primitive_check(integer_modulus,exercise["f"],polynomial_modulus)}
    return {"answer": None}


def solve_from_file(exercise_location: str):
    with open(exercise_location, "r") as exercise_file:
        exercise = json.load(exercise_file)

    return solve(exercise)


def save_answer_to_file(answer_location: str, answer: object):
    with open(answer_location, "w") as answer_file:
        json.dump(answer, answer_file, indent=4)


def solve_exercise(exercise_location: str, answer_location: str):
    answer = solve_from_file(exercise_location)

    save_answer_to_file(answer_location, answer)
