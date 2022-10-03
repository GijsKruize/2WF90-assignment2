##
# 2WF90 Algebra for Security -- Software Assignment 2
# Polynomial and Finite Field Arithmetic
# solve.py
#
#
# Group number:
# group_number
#
# Author names and student IDs:
# Gijs Kruize (1658662)
# Christian Groothuis (1715534)
# Jordy Verhoeven (1001249)
# Niels Boonstra (1451294)
##
# Import built-in json library for handling input/output
import json


def solve(exercise: object):
    exercise_type = exercise["type"]
    exercise_task = exercise["task"]
    integer_modulus = exercise["integer_modulus"]
    f = exercise["f"]

    print(exercise_type, exercise_task, integer_modulus, f)
    ### Parse and solve ###
    # Check type of exercise
    if exercise_type == "polynomial_arithmetic":
        # Check what task within the polynomial arithmetic tasks we need to perform
        if exercise_task == "addition":
            from polynomial_arithmetic.add import addition
            return {"answer": addition(integer_modulus, f, exercise["g"])}
        elif exercise_task == "subtraction":
            # Solve polynomial arithmetic subtraction exercise
            pass
        # et cetera
    elif exercise_type == "finite_field_arithmetic":
        # Check what task within the finite field arithmetic tasks we need to perform
        if exercise_task == "addition":
            # Solve finite field arithmetic addition exercise
            pass


def solve_from_file(exercise_location: str) -> object:
    with open(exercise_location, "r") as exercise_file:
        exercise = json.load(exercise_file)

    return solve(exercise)


def save_answer_to_file(answer_location: str, answer: object):
    with open(answer_location, "w") as answer_file:
        json.dump(answer, answer_file, indent=4)


def solve_exercise(exercise_location: str, answer_location: str):
    answer = solve_from_file(exercise_location)

    save_answer_to_file(answer_location, answer)
