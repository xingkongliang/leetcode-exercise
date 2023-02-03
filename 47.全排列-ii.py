#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
from typing import List
import copy

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if size == depth:
                if path not in res:
                    res.append(copy.copy(path))
                return 
            
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth+1, path, used, res)
                    used[i] = False
                    path.pop()
            return res

        size = len(nums)
        if len(nums) == 0:
            return []
        
        res = []
        res_set = []
        path = []
        used = [False for _ in range(size)]
        dfs(nums, size, 0, path, used, res)

        return res


if __name__ == '__main__':
    nums = [1,1,2]
    solution = Solution()
    res = solution.permuteUnique(nums)
    print(res)
# @lc code=end

