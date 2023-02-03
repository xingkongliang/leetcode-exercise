from typing import List

def coinChange(coins: List[int], amount: int):
    def dp(n):
        # base case
        if n == 0: return 0
        if n < 0: return -1
        # 求最小值，所以初始化正无穷
        res = float('inf')
        for coin in coins:
            subproblem = dp(n-coin)
            # 子问题无解，跳过
            if subproblem == -1: continue
            res = min(res, 1+subproblem)
        
        return res if res != float('inf') else -1
    return dp(amount)


def coinChange_memo(coins: List[int], amount: int):
    memo = dict()
    def dp(n):
        if n in memo: return memo[n]
        # base case
        if n == 0: return 0
        if n < 0: return -1
        # 求最小值，所以初始化正无穷
        res = float('inf')
        for coin in coins:
            subproblem = dp(n-coin)
            # 子问题无解，跳过
            if subproblem == -1: continue
            res = min(res, 1+subproblem)
        memo[n] = res if res != float('inf') else -1
        return memo[n]
    
    return dp(amount)


print(coinChange_memo([1,2,5], 11))