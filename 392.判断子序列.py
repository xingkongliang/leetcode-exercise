#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                # f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]
                if ord(t[i]) == j + ord('a'):
                    f[i][j] = i
                else:
                    f[i][j] = f[i + 1][j]
        
        add = 0
        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1
        
        return True

S = Solution()
print(S.isSubsequence(s = "abc", t = "ahbgdc"))

# @lc code=end

