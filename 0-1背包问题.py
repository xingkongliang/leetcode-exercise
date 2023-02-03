
from typing import List

def knapsack(W:int, wt: List[int], val: List[int]):
    N = len(wt)
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(N+1):
        for w in range(W+1):
            if w - wt[i-1] < 0:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i-1]]+val[i-1])
    print(dp)
    return dp[N][W]


def knapsack2(V: int, n: int, vw: List[List[int]]) -> int:
    # write code here
    dp = [[0 for _ in range(V+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for w in range(1, V+1):
            if w - vw[i-1][0] < 0:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-vw[i-1][0]]+vw[i-1][1])
    print(dp)
    return dp[n][V]

# print(knapsack(W=4, wt=[2,1,3], val=[4,2,3]))
print(knapsack2(10,2,[[1,3],[10,4]]))

N * M 军阵