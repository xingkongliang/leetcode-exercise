#
# @lc app=leetcode.cn id=819 lang=python3
#
# [819] 最常见的单词
#
from typing import List
# @lc code=start
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         import collections
#         count = collections.defaultdict(int)
#         word, n = "", len(paragraph)
#         for i in range(n+1):
#             if i<n and paragraph[i].isalpha():
#                 word += paragraph[i].lower()
#             elif word:
#                 count[word.lower()] += 1
#                 word = ""

#         maxcount = 0
#         maxworld = ""
#         for key, value in count.items():
#             if value > maxcount and key not in banned:
#                 maxworld = key
#                 maxcount = value

#         return maxworld

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import collections
        ban = set(banned)
        freq = collections.Counter()
        word, n = "", len(paragraph)
        for i in range(n + 1):
            if i < n and paragraph[i].isalpha():
                word += paragraph[i].lower()
            elif word:
                if word not in ban:
                    freq[word] += 1
                word = ""
        maxFreq = max(freq.values())
        return next(word for word, f in freq.items() if f == maxFreq)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
S = Solution()
print(S.mostCommonWord(paragraph, banned))
# @lc code=end

