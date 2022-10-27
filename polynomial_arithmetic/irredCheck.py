from polynomial_arithmetic.euclid import euclid
from polynomial_arithmetic.long_division import long_division

def irreducibleTest(p,f):
    n = len(f)-1
    list_of_primes=findPrimes(n)
    k=len(list_of_primes)
    list_div=[]
    m=0;
    while m<k:
        list_div.append(int(n/list_of_primes[m]))
        m= m + 1

    for x in list_div:
        degreeG = pow(p, x)
        g = [0] * (degreeG)
        g[0] = 1
        g[degreeG - 2] = p-1
        a,b,answer=euclid(p,f, g)

        if answer !=[1]:
            return False

    degreek = pow(p, n)
    k = [0] * (degreek)
    k[0] = 1
    k[degreek - 2] = -1
    q,r=long_division[p, k, f]
    if all(item == 0 for item in q):
        return True
    return True


def findPrimes(n):
    list=[]
    i=2
    while n>1:
        if n % i == 0:
            list.append(i)
            n= n / i
            i= i - 1
        i= i + 1
    return list