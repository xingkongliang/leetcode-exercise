from typing import List

class Solution:
   def equalPartition(self, N, arr):
       def solve(arr, n, tot):
           if n== 0 and tot > 0:
               return False
           if tot == 0:
               return True
           if arr[n-1] > tot:
               return  solve(arr , n-1 ,tot)
           else:
               return solve(arr, n-1, tot) or solve(arr, n-1, tot-arr[n-1])

       tot = sum(arr)
       if tot % 2 != 0:
           return False
       tot = int(tot/2)
       return solve(arr, N ,tot)

class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum & 1: return False
        half_sum = total_sum // 2
        dp = [True] + [False]*half_sum
        for num in nums:
            for j in range(half_sum, num-1, -1):
                dp[j] |= dp[j-num]
            if dp[half_sum]:
                return True
        return dp[half_sum]
        


a = Solution()
print(a.equalPartition(4, [1, 11, 5, 5]))

a = Solution2()
print(a.canPartition([1, 11, 5, 5]))