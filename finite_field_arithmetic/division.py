from polynomial_arithmetic.long_division import long_division
from finite_field_arithmetic.multiply import multiplication
from finite_field_arithmetic.inversion import inversion

def division(mod,h,f,g):

    if all(item == 0 for item in f):
        return "null"
    if all(item == 0 for item in g):
        return "null"

    q,r= long_division(mod,f,g)
    if all(item == 0 for item in r):
        return q
    else:
        inverse_g=inversion(mod,h,g)
        if inverse_g == "error":
            return "null"
        answer=multiplication(mod,h,f,inverse_g)

        return answer
