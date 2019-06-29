""" 215. Kth Largest Element in an Array - Medium
##devide and conquer #heap
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.

 """

import random


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)
            pos = self.partition(left, right, pivot_idx, nums)
            if pos == k - 1:
                return nums[pos]
            elif pos > k - 1:
                right = pos - 1
            else:
                left = pos + 1

    def partition(self, left, right, pivot_idx, nums):
        pivot_val = nums[pivot_idx]
        new_pivot_idx = left
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        for i in range(left, right):
            if nums[i] > pivot_val:
                nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                new_pivot_idx += 1
        nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
        return new_pivot_idx


if __name__ == "__main__":
    res = Solution().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2)
    print(res)
