""" 96. Unique Binary Search Trees - Medium
#dynamic programming #tree

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3 """


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1, 1]
        for i in range(2, n + 1):
            val = 0
            for j in range(i):
                val += dp[j] * dp[i - j - 1]
            dp.append(val)

        return dp[-1]


if __name__ == "__main__":
    print(Solution().numTrees(n=3))