"""
Topic: array - medium
Related:
    46. Permutations (Medium)
    47. Permutations II (Medium)
    60. Permutation Sequence (Medium)
    266. Palindrome Permutation II (Medium)

Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible
order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding
outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1 """


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p = -1
        q = 0
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                p = i
        if p == -1:
            nums.reverse()
        for i in range(p + 1, len(nums)):
            if nums[i] > nums[p]:
                q = i
        nums[p], nums[q] = nums[q], nums[p]
        nums[p + 1:] = nums[:p:-1]


if __name__ == "__main__":
    nums = [1, 7, 3, 4, 2, 1]
    Solution().nextPermutation(nums)
    print(nums)