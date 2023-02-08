#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    cnt = 0
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        next_i, next_j = i + di, j + dj
                        if next_i < 0 or next_j < 0 or next_i >= m or next_j >= n or not grid[next_i][next_j]:
                            cnt += 1
                    ans += cnt
        return ans
# @lc code=end

