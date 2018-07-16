from math import sqrt

N = 20

def factorize(x):
    x_factors = []
    for i in range(2, int(sqrt(x))+1):
        while x % i == 0:
            x_factors.append(i)
            x = x//i
    res_dict = dict(map(lambda x  : (x , list(x_factors).count(x)), x_factors))
    return res_dict if len(res_dict) > 0 else {x: 1}

fact_counts = {1: 1}

for x in range(2, N+1):
    # print("x = {}".format(x))
    x_factors = factorize(x)
    # print("x-factors = {}".format(x_factors))
    for f, c in x_factors.items():
        if f not in fact_counts:
            fact_counts[f] = c
        else:
            fact_counts[f] = max(fact_counts[f], c)
    # print("x-fact_counts = {}".format(fact_counts))

res = 1
for k, v in fact_counts.items():
    res = res * (k**v)

print(res)