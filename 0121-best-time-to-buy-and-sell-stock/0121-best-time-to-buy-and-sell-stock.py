class Solution(object):
    def maxProfit(self, prices):
        buy = 0
        sell = 1
        profit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                maxprofit = prices[sell] - prices[buy]
                profit = max(profit,maxprofit)
            else:
                buy = sell
            sell +=1
        return profit

        