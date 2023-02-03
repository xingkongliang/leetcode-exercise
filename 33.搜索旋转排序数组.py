#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            pivot = low + (high - low) // 2
            if nums[pivot] == target:
                return pivot
            if nums[0] <= nums[pivot]:
                if nums[0] <= target < nums[pivot]:
                    high = pivot - 1
                else:
                    low = pivot + 1
            else:
                if nums[pivot] < target <= nums[-1]:
                    low = pivot + 1
                else:
                    high = pivot - 1
        return -1

S = Solution()
print(S.search([1,3], 3))
# @lc code=end

