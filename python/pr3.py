# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
#N = 13195
N = 600851475143

largest_factor = 1
for factor in range(2, int(sqrt(N))+1):
    while (N % factor == 0):
        largest_factor = factor
        N = int(N / factor)

print(largest_factor)