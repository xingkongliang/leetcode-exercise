import math
m = 4
target = m**3
for i in range(target):
    count = 0
    for j in range(m):
        count += (i + 2*j)
    if count == target:
        out = [(i + j) for j in range(m)]
        print('+'.join(map(str, out)))