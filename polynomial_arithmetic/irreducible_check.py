from polynomial_arithmetic.euclidean import euclidean


def irreducible_test(f, p):
    n = len(f) - 1
    list_of_primes = find_primes(n)
    k = len(list_of_primes)
    list_div = [n]
    m = 0

    while m < k:
        list_div.append(int(n / list_of_primes[m]))
        m = m + 1

    for x in list_div:
        degree_g = pow(p, x)
        g = [0] * (degree_g)
        g[0] = 1
        g[degree_g - 2] = -1
        answer = euclidean[f, g, p]

        if answer != 1:
            return False

    return True


def find_primes(n):
    primes = []
    i = 2

    while n > 1:
        if n % i == 0:
            primes.append(i)
            n = n / i
            i = i - 1

        i = i + 1

    return primes
