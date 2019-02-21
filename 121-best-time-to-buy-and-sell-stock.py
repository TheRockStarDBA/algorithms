""" 121. Best Time to Buy and Sell Stock － Easy
topic: array, dynamic programming


Say you have an array for which the ith element is the price of a given stock on
day i.

If you were only permitted to complete at most one transaction (i.e., buy one
and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0. """

# Approach 1: Dynamic Programming
# We can make sure the max profit at least be ZERO. So,
# 1) we have two pointers (start & end )
# 2) if prices[end] - prices[start] >  0, then move the "end" pointer to next
# 3) if prices[end] - prices[start] <= 0, then move the "start" pointer to current posstion.
# 4) tracking the max profit

# Time:  O(n)
# Space: O(1)


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0

        profit, delta = 0, 0
        start, end = 0, 0
        for i in range(len(prices)):
            end = i
            delta = prices[end] - prices[start]
            if delta <= 0:
                start = i
            profit = max(profit, delta)

        return profit


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([7, 6, 4, 3, 1]))
