""" 26. Remove Duplicates from Sorted Array - Easy
Topic: Array, Two-Pointers
Related: Remove Element - Easy
Remove Duplicates from Sorted Array II - Medium

Given a sorted array nums, remove the duplicates in-place such that each element
 appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the
 input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums
being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums
being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
 """

# Approach: Two Pointers
# Algorithm

# Since the array is already sorted, we can keep two pointers i and j, where i
# is the slow-runner while j is the fast-runner. As long as nums[i] = nums[j],
# we increment j to skip the duplicate.

# When we encounter nums[j] != nums[i], the duplicate run has ended so we must
# copy its value to nums[i + 1]. i is then incremented and we repeat
# the same process again until j reaches the end of array.

# Time:  O(n)
# Space: O(1)


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(nums))