

from finite_field_arithmetic.multiply import multiplication


def primitive_check(mod, polynom, polynomial_modulus):
    q = mod ** (len(polynom)-1)
    prime_divs = prime_factorization(q-1)
    k=len(prime_divs)
    i=1

    while i <= k and compute_power(mod, polynom, polynomial_modulus, prime_divs, q, i):
        i = i+1
    
    return i > k

def compute_power(mod, polynom, polynomial_modulus, prime_divs, q, i):
    i = i-1 #this makes shure we start at index 0 instead of 1
    power = ((q-1)/prime_divs[i])
    pol_mod_mult = polynomial_modulus #initialise a^1

    for _ in range(int(power-1)):
        z,pol_mod_mult = multiplication(mod, polynomial_modulus,polynom, pol_mod_mult)
    
    return z != "1"

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