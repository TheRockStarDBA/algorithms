""" 55. Jump Game
Topics: array, greedy - medium
Related: Jump Game II - Hard

Description:

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Input: [2,3,1,1,4]

Output: true

Assumptions:
non-negative integers
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums:
            return False

        idx = 0
        dest = nums[0]
        while idx <= dest:
            if dest >= (len(nums) - 1):
                return True
            dest = max(dest, idx + nums[idx])
            idx += 1
        return False


if __name__ == "__main__":
    print(Solution().canJump([2, 3, 1, 1, 4]))
    print(Solution().canJump([3, 2, 1, 0, 4]))