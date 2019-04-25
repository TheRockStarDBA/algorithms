"""
322. Coin Change

#dynamic programming

You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up
that amount. If that amount of money cannot be made up by any combination of the
coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
 """


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        if coins is None or len(coins) == 0:
            return -1

        INF = 0x7fffffff
        dp = [INF] * (amount + 1)
        dp[0] = 0
        coins.sort()

        for i in range(amount + 1):
            if dp[i] != INF:
                for coin in coins:
                    if i + coin <= amount:
                        dp[i + coin] = min(dp[i] + 1, dp[i + coin])

        return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    print(Solution().coinChange(coins=[1, 2, 5], amount=11))
