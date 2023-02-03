#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
from typing import List
# @lc code=start
class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if n == 0:
    #         return 0
    #     dp = [1 for _ in range(n)]
    #     for i in range(n):
    #         for j in range(i):
    #             if nums[j] < nums[i]:
    #                 dp[i] = max(dp[i], dp[j]+1)
    #     return max(dp)
    import bisect
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = nums
        dp = [1]*len(l) # 初始化dp，最小递增子序列长度为1
        arr = [l[0]] # 创建数组
        for i in range(1,len(l)): # 从原序列第二个元素开始遍历
            if l[i] > arr[-1]:
                arr.append(l[i])
                dp[i] = len(arr)
            else:
                pos = bisect.bisect_left(arr, l[i]) # 用二分法找到arr中第一个比ele_i大（或相等）的元素的位置
                arr[pos] = l[i]
                dp[i] = pos+1
        return max(dp)


S  = Solution()
print(S.lengthOfLIS(nums=[1,3,6,7,9,4,10,5,6]))
# @lc code=end

