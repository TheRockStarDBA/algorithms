""" Search for a range 

Find First and Last Position of Element in Sorted Array

Description:

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

Input: [5, 7, 7, 8, 8, 10] and target value 8

Output: [3, 4]

Assumptions:

If the target is not found in the array, return [-1, -1] """

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums)-1

        while True:
            if nums[start]>target or nums[end]<target:
                return[-1,-1]
            
            mid = start+(end-start)/2
            if 

