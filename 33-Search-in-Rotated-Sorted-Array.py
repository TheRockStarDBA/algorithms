"""
33. Search in Rotated Sorted Array (Medium)
Topic: binary-search, array;

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1 """

# Approach : Binary search
# The problem is to implement a search in O(log(N)) time that gives an idea to use a binary search.

# The algorithm is quite straightforward :

# Find a rotation index rotation_index, i.e. index of the smallest element in the array. Binary search works just perfect here.

# rotation_index splits array in two parts. Compare nums[0] and target to identify in which part one has to look for target.

# Perform a binary search in the chosen part of the array.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
