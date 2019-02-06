"""
Permutations II
Topic: backtracking - medium

Description:

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Input: [1,1,2]

Output: [[1,1,2],[1,2,1],[2,1,1]]
 """


class Solution(object):
    # using set to exclude repeted numbers
    def permuteUnique(self, nums):
        res = []
        if len(nums) == 0:
            return res
        self.get_permute(nums, res, [])
        return res

    def get_permute(self, nums, res, current):
        if not nums:
            res.append(current + [])
            return
        appeared = set()
        for i in range(len(nums)):
            if nums[i] in appeared:
                continue
            appeared.add(nums[i])
            current.append(nums[i])
            self.get_permute(nums[:i] + nums[i + 1:], res, current)
            current.pop()


class Solution2(object):
    # using sorting and compare consecutive two numbers
    def permuteUnique(self, nums):
        res = []
        if len(nums) == 0:
            return res
        sorted(nums)
        self.get_permute(nums, res, [])
        return res

    def get_permute(self, nums, res, current):
        if not nums:
            res.append(current + [])
            return

        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])
            self.get_permute(nums[:i] + nums[i + 1:], res, current)
            current.pop()


if __name__ == "main":
    nums = [1, 1, 2]
    result = Solution().permuteUnique(nums)
    print(result)
