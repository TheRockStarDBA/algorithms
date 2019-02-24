""" 128. Longest Consecutive Sequence - Hard
topic: array, union find
related: Binary Tree Longest Consecutive Sequence - Medium

Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore
its length is 4. """


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in nums_set:
                current_num = num
                current_length = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_length += 1

            longest = max(longest, current_length)

        return longest


class Solution2(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        longest = 1
        current = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current += 1
                else:
                    longest = max(longest, current)
                    current = 1
        return max(longest, current)


if __name__ == "__main__":
    longest = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
    print(longest)