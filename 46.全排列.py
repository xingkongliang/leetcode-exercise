#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import List
import copy
# @lc code=start

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if size == depth:
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
        path = []
        used = [False for _ in range(size)]
        dfs(nums, size, 0, path, used, res)

        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    res = solution.permute(nums)
    print(res)


# @lc code=end

