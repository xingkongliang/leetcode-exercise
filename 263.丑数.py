#
# @lc app=leetcode.cn id=263 lang=python3
#
# [263] 丑数
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factor = [2, 3, 5]
        for f in factor:
            while n % f == 0:
                n = n // f
        return n == 1
# @lc code=end

