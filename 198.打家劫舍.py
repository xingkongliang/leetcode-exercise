#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
from typing import List
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        states = [0 for _ in range(len(nums))]
        states[0] = nums[0]
        states[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            states[i] = max(states[i-1], states[i-2]+nums[i])
        return states[-1]

S = Solution()
print(S.rob([2,7,9,3,1]))  
# @lc code=end

