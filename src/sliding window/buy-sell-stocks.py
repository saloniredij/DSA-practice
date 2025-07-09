'''
Best Time to Buy and Sell Stock
Solved 
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.


Example 1:
Input: prices = [10,1,5,6,7,1]
Output: 6

Example 2:
Input: prices = [10,8,7,5,2]
Output: 0

Constraints:
1 <= prices.length <= 100
0 <= prices[i] <= 100
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i,j=0,1
        while i < j and i < len(prices) and j < len(prices):
            pp,sp = prices[i],prices[j]
            if prices[i] < prices[j]:
                maxProfit = max(maxProfit, prices[j] - prices[i])
            else:
                i = j
            j += 1
        return maxProfit