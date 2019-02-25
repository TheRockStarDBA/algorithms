""" 152. Maximum Product Subarray - Medium
topic: array, dynamic programming
related:    Maximum Subarray - Easy
            House Robber - Easy
            Product of Array Except Self - Medium
            Maximum Product of Three Numbers - Easy
            Subarray Product Less Than K - Medium

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 """


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max, local_min = 1, 1
        max_product = 1
        for num in nums:
            local_max = max(num, local_max * num, local_min * num)
            local_min = min(num, local_max * num, local_min * num)
            max_product = max(local_max, max_product)

        return max_product


if __name__ == "__main__":
    nums1 = [2, 3, -2, 4]
    nums2 = [6, -3, -10, 0, 2]
    print(Solution().maxProduct(nums1))
    print(Solution().maxProduct(nums2))
