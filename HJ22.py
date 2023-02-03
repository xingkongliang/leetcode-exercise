import sys

while True:
    n = int(input())
    if n == 0: break
    res = 0
    last = 0
    while n // 3 != 0 :
        carry = n // 3
        res += carry
        last = n % 3
        n = last + carry 
    if n == 2:
        res += 1
    print(res)


