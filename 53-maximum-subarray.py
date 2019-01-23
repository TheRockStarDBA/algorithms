""" 53. Maximum Subarray

Topics: array, divide and conquer, dynamic programming (Easy)

Related: Best Time to Buy and Sell Stock - Easy
Maximum Product Subarray - Medium
Degree of an Array -Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and
 return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is
more subtle. """


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = temp = nums[0]

        for num in nums[1:]:
            temp = max(num, temp + num)
            largest = max(temp, largest)

        return largest
