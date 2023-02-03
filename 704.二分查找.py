#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            n = (left + right) // 2
            if nums[n] < target:
                left = n + 1
            elif nums[n] > target:
                right = n - 1
            else:
                return n
        return -1
                
S = Solution()
print(S.search(nums = [-1,0,3,5,9,12], target = -1))
# @lc code=end

