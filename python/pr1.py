def is_35mult(x):
    return x % 3 == 0 or x % 5 == 0
N=1000
sum = 0
for i in range(0,N):
    if is_35mult(i):
        sum = sum + i

print(sum)