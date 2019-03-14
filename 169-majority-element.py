""" 169. Majority Element - Easy
Topic: array, divide and conqure, bit manipulation
Related: Majority Element II - Medium

Given an array of size n, find the majority element. The majority element is the
element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist
in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
 """

import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter_list = collections.Counter(nums).items()
        counter_list = sorted(counter_list, key=lambda a: a[1], reverse=True)
        return counter_list[0][0]


class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        most_common_item_counter = collections.Counter(nums).most_common(1)
        return most_common_item_counter[0][0]


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = Solution().majorityElement(nums)
    print(result)
