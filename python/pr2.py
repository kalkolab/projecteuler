# even Fibonacci numbers
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

sum = 0
f0 = 1
f1 = 2

while (f1 <= 4_000_000):
    if (f1 % 2 ==0):
        sum = sum + f1
    t = f1
    f1 = f1 + f0
    f0 = t

print(sum)