#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
from typing import List
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rangeRob(nums):
            first = nums[0]
            second = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                first, second = second, max(second, first + nums[i])
            return second
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(rangeRob(nums[0:-1]), rangeRob(nums[1:]))
S = Solution()
print(S.rob([1,3,1,3,100]))
# @lc code=end

