#
# @lc app=leetcode.cn id=1329 lang=python3
#
# [1329] 将矩阵按对角线排序
#
from typing import List
import collections
# @lc code=start
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                dic[i-j].append(mat[i][j])
        
        for key in dic:
            dic[key] = sorted(dic[key], reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j] = dic[i-j].pop()
        return mat

if __name__ == '__main__':
    S = Solution()
    print(S.diagonalSort(mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
# @lc code=end

