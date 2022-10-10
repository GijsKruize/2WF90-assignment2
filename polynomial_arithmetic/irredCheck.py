def irreducibleTest(f, p):
    n = len(f)-1
    list_of_primes=findPrimes(n)
    k=len(list_of_primes)
    list_div=[n]
    m=0;
    while m<k:
        list_div.append(int(n/list_of_primes[m]))
        m= m + 1

    for x in list_div:
        degreeG = pow(p, x)
        g = [0] * (degreeG)
        g[0] = 1
        g[degreeG - 2] = -1
        answer=poly_euclid[f, g, p]
        if answer !=1:
            return False
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