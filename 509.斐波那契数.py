#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        def helper(memo, n):
            if n == 1 or n==2:
                return 1
            if memo[n] != 0:
                return memo[n]
            else:
                memo[n] = helper(memo, n-1) + helper(memo, n-2)
                return memo[n]
        if n == 0: return 0
        memo = [0 for _ in range(n+1)]
        return helper(memo, n)
S = Solution()
print(S.fib(0))
# @lc code=end

