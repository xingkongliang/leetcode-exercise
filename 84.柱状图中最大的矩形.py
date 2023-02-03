#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

from typing import List
# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack[-1]] = i
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n))

        return ans

S = Solution()
print(S.largestRectangleArea(heights = [2,1,5,6,2,3]))
# @lc code=end

