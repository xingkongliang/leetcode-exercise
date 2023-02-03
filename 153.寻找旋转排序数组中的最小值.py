#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
from typing import List
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:    
        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]

S = Solution()
print(S.findMin([2,1]))
# @lc code=end

