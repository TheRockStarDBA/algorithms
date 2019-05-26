""" 209. Minimum Size Subarray Sum - Medium
##array #two pointers #binary search

Given an array of n positive integers and a positive integer s, find the minimal
length of a contiguous subarray of which the sum ≥ s. If there isn't one, return
0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which
the time complexity is O(n log n).
 """

# two pointers
# Time:  O(n)
# Space: O(1)


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        current_sum = 0
        min_size = float("inf")

        for i in range(len(nums)):
            current_sum += nums[i]
            while current_sum >= s:
                min_size = min(min_size, i - start + 1)
                current_sum -= nums[start]
                start += 1

        return min_size if min_size != float('inf') else 0


if __name__ == "__main__":
    ans = Solution().minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3])
    print(ans)