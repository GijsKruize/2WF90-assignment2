import random
from irredCheck import irreducibleTest

def findIrred(n, p):
    f = [random.randint(1, p-1)]
    i=0
    while i<n-1:
        f.append(random.randint(0, p - 1))

    irreducible=False
    while not irreducible:
        if irreducibleTest(f,p):
           irreducible = True
        else:
            f = [random.randint(1, p - 1)]
            i = 0
            while i < n-1:
                f.append(random.randint(0, p - 1))

    return f