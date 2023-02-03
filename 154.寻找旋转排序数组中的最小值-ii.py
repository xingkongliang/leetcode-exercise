#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        while low < high:
            mid = low + (high-low) // 2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high -= 1
        return nums[low]

S = Solution()
print(S.findMin([3,3,1,3]))
# @lc code=end

