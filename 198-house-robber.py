""" 198. House Robber - Easy

# dynamic programming

You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security system connected and
it will automatically contact the police if two adjacent houses were broken into
on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without alerting
the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
 """

#  Approach:  Dynamic Programming

#    We can easy find the recurive fomular:

#        dp[n] = max(
#                       dp[n-1],   // the previous house has been robbed.
#                       dp[n-2] + money[n]  // the previous house has NOT been robbed.
#                   )

#    The initalization is obvious:
#        dp[1] = money[1]
#        dp[2] = max(money[1], money[2])


class Solution(object):
    def rob(self, money):
        """
        :type money: List[int]
        :rtype: int
        """
        n = len(money)
        if n == 0:
            return 0
        dp = [0] * n
        if n >= 1:
            dp[0] = money[0]
        if n >= 2:
            dp[1] = max(money[0], money[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + money[i])

        return dp[n - 1]


class Solution2(object):
    def rob(self, money):
        """
        :type money: List[int]
        :rtype: int
        """
        temp = [0, 0]
        for n in money:
            temp[0], temp[1] = max(temp), n + temp[0]

        return max(temp)


if __name__ == "__main__":
    money = [2, 7, 9, 3, 1]
    result = Solution().rob(money)
    print(result)
