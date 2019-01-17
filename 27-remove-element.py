""" 27. Remove Element
Topics: Array, Two-Pointers (Easy)

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
 """

# Approach: Two Pointers

# Intuition

# Since question asked us to remove all elements of the given value in-place, we have to handle it with O(1)s extra space.
# To solve it, We can keep two pointers i and j, where i is the slow-runner while j is the fast-runner.

# Algorithm

# When nums[j] equals to the given value, skip this element by incrementing j. As long as nums[j]!= val, we copy nums[j] to nums[i]
#  and increment both indexes at the same time. Repeat the process until j reaches the end of the array and the new length is i.


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i


print(Solution().removeElement(nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2))

# Complexity analysis
# Time complexity : O(n). Assume the array has a total of n elements, both i and j traverse at most 2n steps.
# Space complexity : O(1).
