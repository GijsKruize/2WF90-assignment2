

from finite_field_arithmetic.multiply import multiplication


def primitive_check(mod, polynom, a):
    q = mod ** (len(polynom)-1)
    prime_divs = prime_factorization(q-1)
    k=len(prime_divs)
    i=1

    while 1 <= k and compute_power(mod, polynom, a, prime_divs, q, i):
        i = i+1
    
    if i <= k:
        return False
    else:
        return True

def compute_power(mod, polynom, a, prime_divs, q, i):
    j = i-1 #this makes shure we start at index 0 instead of 1
    power = ((q-1)/prime_divs[j])
    a_mult = a #initialise a^1

    for x in range(int(power-1)):
        z,a_mult = multiplication(mod, polynom, a_mult)
    
    if z== "1":
        return False
    else:
        return True

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