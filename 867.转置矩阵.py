#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#
from typing import List
# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        transposed = [[0 for _ in range(m)] for _ in range(n)]
        print(transposed)
        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]
        return transposed

S = Solution()
print(S.transpose([[1,2,3],[4,5,6]]))
# @lc code=end

