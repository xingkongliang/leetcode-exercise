#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#
from typing import List
# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        first = -1
        maxvalue = -1
        secondvalue = -1
        for i, value in enumerate(nums):
            if value > maxvalue:
                secondvalue = maxvalue
                maxvalue = value
                first = i
            elif value > secondvalue:
                secondvalue = value
        if maxvalue >= secondvalue * 2:
            return first
        else:
            return -1

S = Solution()
print(S.dominantIndex([1,2,3,4]))
# @lc code=end

