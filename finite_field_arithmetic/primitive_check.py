
import random
from finite_field_arithmetic.multiply import multiplication


def primitive_check(mod, polynom, polynomial_modulus):
    q = mod ** (len(polynomial_modulus)-1)
    prime_divs = prime_factorization(q-1)
    k=len(prime_divs)
    i=1

    while i <= k and compute_power(mod, polynom, polynomial_modulus, prime_divs, q, i):
        i = i+1
    
    return i > k

def compute_power(mod, polynom, polynomial_modulus, prime_divs, q, i):
    i = i-1 #this makes shure we start at index 0 instead of 1
    power = ((q-1)/prime_divs[i])
    pol_mod_mult = polynom #initialise a^1

    for _ in range(int(power-1)):
        pol_mod_mult = multiplication(mod, polynomial_modulus,polynom, pol_mod_mult)[1]
    
    return pol_mod_mult != [1]

def prime_factorization(f):
    primes = []

    prime = 2
    while f >= prime*prime:
        if f % prime == 0:
            primes.append(prime)
            f = f / prime
        else:
            prime = prime + 1

    primes.append(int(f))
    return primes


def generate_primitve_element(mod, polynomial_mod):
    a = []
    a_check = []
    for _ in range(len(polynomial_mod)-1):
        a.append(random.randint(0,mod))

    for _ in range(len(polynomial_mod)-1):
        a_check.append(0)

    while primitive_check(mod, a, polynomial_mod) == False:
        for i in (len(a)):
            a[i]=(random.randint(0,mod))
        while a == a_check:
            for i in (len(a)):
                a[i]=(random.randint(0,mod))

    return a
