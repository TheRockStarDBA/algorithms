"""
33. Search in Rotated Sorted Array
Topic: binary-search, array; (Medium Level)

Suppose an array sorted in ascending order is rotated at some pivot unknown to 
you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, 
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

# Approach : Binary search
# The problem is to implement a search in O(log(N)) time that gives an idea to 
# use a binary search.

# The algorithm is quite straightforward :

# Find a rotation index rotation_index, i.e. index of the smallest element in 
# the array. Binary search works just perfect here.

# rotation_index splits array in two parts. Compare nums[0] and target to identify 
# in which part one has to look for target.

# Perform a binary search in the chosen part of the array.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find_rotation_index(left, right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        def search_target(left, right):
            # Binary search
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                else:
                    if target < nums[pivot]:
                        right = pivot - 1
                    else:
                        left = pivot + 1
            return -1

        n = len(nums)

        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_index = find_rotation_index(0, n - 1)

        #if target is the smallest number
        if nums[rotate_index] == target:
            return rotate_index
        #if array is not rotated, search the entire array:
        if rotate_index == 0:
            return search_target(0, n - 1)
        if target < nums[0]:
            # search on the right side
            return search_target(rotate_index, n - 1)
        # search on the left side
        return search_target(0, rotate_index)

if __name__ == "__main__":
    print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))
    print(Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))
