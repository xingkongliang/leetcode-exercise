#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
from typing import List
import copy
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = ["."*n for _ in range(n)]
        def backtrack(board, row):
            if row == n:
                res.append(copy.copy(board))
                return

            for col in range(n):
                if not isValid(board, row, col):
                    continue
                temp = list(board[row])
                temp[col] = 'Q'
                board[row] = ''.join(temp)
                backtrack(board, row+1)
                temp = list(board[row])
                temp[col] = '.'
                board[row] = ''.join(temp)

        def isValid(board, row, col):
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
                
                for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
                    if board[i][j] == 'Q':
                        return False
                for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
                    if board[i][j] == 'Q':
                        return False
            return True
        
        backtrack(board, 0)
        return res


S = Solution()
print(S.solveNQueens(4))

# @lc code=end

