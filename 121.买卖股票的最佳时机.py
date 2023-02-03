#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        minprice = float("inf")
        for price in prices:
            maxprofit = max(price-minprice, maxprofit)
            minprice = min(minprice, price)
        return maxprofit
# @lc code=end

