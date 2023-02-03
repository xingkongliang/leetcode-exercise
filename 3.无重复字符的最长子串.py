#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         # 哈希集合，记录每个字符是否出现过
        occ = set()
        rk = -1
        ans = 0
        n = len(s)
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while rk + 1 < n and s[rk+1] not in occ:
                occ.add(s[rk+1])
                rk += 1
            ans = max(ans, rk-i+1)
        return ans

S = Solution()
ans = S.lengthOfLongestSubstring("pwwkew")
print(ans)
# @lc code=end

