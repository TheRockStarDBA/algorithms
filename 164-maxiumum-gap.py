""" 164. Maximum Gap - Hard
##sort

Given an unsorted array, find the maximum difference between the successive
elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in
the 32-bit signed integer range.
Try to solve it in linear time/space. """

# Approach 1: Comparison Sorting
# Sort the entire array. Then iterate over it to find the maximum gap between
# two successive elements.
# Time:  O(nlogn)
# Space: O(n)


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # check if array is empty or small sized
        if len(nums) < 2:
            return 0

        nums.sort()
        maxGap = float("-inf")
        pre = nums[0]
        for i in nums:
            maxGap = max(maxGap, i - pre)
            pre = i
        return maxGap


if __name__ == "__main__":
    res = Solution().maximumGap([3, 6, 9, 1])
    print(res)