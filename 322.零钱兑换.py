#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
from typing import List
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange_memo(self, coins: List[int], amount: int) -> int:
        memo = dict()
        def dp(n):
            res = float('inf')
            if n in memo: return memo[n]
            if n == 0: return 0
            if n < 0: return -1
            for coin in coins:
                subproblem = dp(n-coin)
                if subproblem == -1: continue
                res = min(res, subproblem+1)
            memo[n] = res if res != float('inf') else -1
            return memo[n]
        return dp(amount)

S = Solution()
print(S.coinChange([1, 2, 5], 11))
# @lc code=end

