
from helpers import prime_factorization


def primitive_check(mod, polynom, a):
    q = mod ** (len(polynom)-1)
    prime_divs = prime_factorization(q-1)
    k=len(prime_divs)
    i=1