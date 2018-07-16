from math import log

n = 10001

max_x = int(n*log(n)+n*log(log(n)))+1

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

print(list(primes_sieve2(max_x))[n-1])
