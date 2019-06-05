""" 646. Maximum Length of Pair Chain - Medium
##dynamic programming #greedy

You are given n pairs of numbers. In every pair, the first number is always smaller
than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c.
Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't
use up all the given pairs. You can select pairs in any order.

Example 1:

Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:

The number of given pairs will be in the range [1, 1000]. """

# Greedy Approach
# Time:  O(nlogn)
# Space: O(1)


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])
        cur, ans = float('-inf'), 0
        for x, y in pairs:
            if cur < x:
                cur = y
                ans += 1
        return ans


if __name__ == "__main__":
    pairs = [[1, 2], [2, 3], [3, 4]]
    print(Solution().findLongestChain(pairs))
