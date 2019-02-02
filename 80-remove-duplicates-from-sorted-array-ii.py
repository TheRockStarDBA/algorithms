""" 80. Remove Duplicates from Sorted Array II - Medium
Topic: array, two-pointers
Related: Remove Duplicates from Sorted Array - Easy
Given a sorted array nums, remove the duplicates in-place such that duplicates
appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the
 input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums
being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums
being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.

} """


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        idx = 1
        twice = False
        while idx < len(nums):
            if nums[idx] != nums[counter] or not twice:
                twice = (nums[counter] == nums[idx])
                counter += 1
                nums[counter] = nums[idx]
            idx += 1

        return counter + 1


if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    result = Solution().removeDuplicates(nums)
    print(result)