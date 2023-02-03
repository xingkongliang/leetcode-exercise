#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
from typing import List
# @lc code=start

     
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        bucket = [0 for _ in range(k)]
        nums.sort()
        nums = nums[::-1]
        def backtrack(nums, index, bucket, target):
            if index == len(nums):
                for i in range(k):
                    if bucket[i] != target:
                        return False
                return True

            for i in range(k):
                if bucket[i] + nums[index] > target:
                    continue

                bucket[i] += nums[index]
                if backtrack(nums, index+1, bucket, target):
                    return True
                bucket[i] -= nums[index]
            return False
            
        if k > len(nums): 
            return False
        sum = 0
        for v in nums:
            sum += v
        if sum % k != 0:
            return False
        
        target = sum / k
        return backtrack(nums, 0, bucket, target)

S = Solution()
print(S.canPartitionKSubsets([114,96,18,190,207,111,73,471,99,20,1037,700,295,101,39,649], 4))
# @lc code=end

