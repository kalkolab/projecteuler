def is_pali(x):
    s = str(x)
    i = 0
    j = len(s) - 1
    while (i<j):
        if (s[i] != s[j]):
            return False
        i = i+1
        j = j-1
    return True

def find():
    max_pali = 0
    for x in range(999, 99, -1):
        for y in range(999, 99, -1):
            prod = x * y
            if is_pali(prod):
                max_pali = max(max_pali, prod)
    return max_pali

# x, y, pali = find()
print(find())
# print(x, y, x*y)