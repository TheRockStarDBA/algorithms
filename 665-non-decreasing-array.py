""" 665. Non-decreasing Array - Easy
##array

Given an array with n integers, your task is to check if it could become non-decreasing
by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:

Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000]. """


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        isChange, prev = False, nums[0]
        for i in range(1, len(nums)):
            if prev > nums[i]:
                if isChange:
                    return False
                if i - 2 < 0 or nums[i - 2] <= nums[i]:
                    prev = nums[i]
                isChange = True
            else:
                prev = nums[i]
        return True


if __name__ == "__main__":
    print(Solution().checkPossibility(nums=[4, 2, 1]))