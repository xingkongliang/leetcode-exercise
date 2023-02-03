import copy
res = []
counts = [0, 0, 0]

def backtrack(counts):
    money = 5*counts[0] + 3*counts[1] + 1/3*counts[2]
    if money >= 100 and sum(counts) != 100:
        return
    elif money != 100 and sum(counts) >= 100:
        return
    elif money == 100 and sum(counts) == 100:
        res.append(copy.copy(counts))
        return
    
    for i in range(3):
        counts[i] += 1
        backtrack(counts)
        counts[i] -= 1
    return res

print(backtrack(counts))

