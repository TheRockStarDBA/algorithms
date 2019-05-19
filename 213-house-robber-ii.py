""" 213. House Robber II - Medium
##dynamic programming

You are a professional robber planning to rob houses along a street. Each house
has a certain amount of money stashed. All houses at this place are arranged in
a circle. That means the first house is the neighbor of the last one. Meanwhile,
adjacent houses have security system connected and it will automatically contact
the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without alerting
the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.


Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Hint:
Since House[1] and House[n] are adjacent, they cannot be robbed together.
Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n],
depending on which choice offers more money. Now the problem has degenerated to
the House Robber, which is already been solved.
 """


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(self.df(nums, 0, len(nums) - 1), \
                    self.df(nums, 1, len(nums)))

    def df(self, nums, start, end):
        prevMax = 0
        currentMax = nums[start]
        for i in range(start + 1, end):
            temp = currentMax
            currentMax = max(prevMax + nums[i], currentMax)
            prevMax = temp
        return currentMax


if __name__ == "__main__":
    maxAmount = Solution().rob(nums=[1, 2, 3, 1])
    print(maxAmount)
