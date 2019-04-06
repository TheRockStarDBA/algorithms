""" 90. Subsets II - Medium
topic: array, backtracking
related: 78. Subsets - Medium

Given a collection of integers that might contain duplicates, nums, return all
possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
] """


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = [[]]
        start = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                # generate all
                start = 0
            size = len(res)
            # use existing subsets to generate new subsets
            for j in range(start, size):
                curr = list(res[j])
                curr.append(nums[i])
                res.append(curr)
            # avoid duplicate subsets
            start = size
        return res


class Solution2(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) == 0 or not nums:
            return res

        nums.sort()
        self.addSubset(nums, res, [], 0)
        return res

    def addSubset(self, nums, res, curr, start):
        res.append(list(curr))
        for i in range(start, len(nums)):
            #if current loop is not the start element, check if it's duplicated with the previous element
            if i != start and nums[i - 1] == nums[i]:
                continue
            curr.append(nums[i])
            self.addSubset(nums, res, curr, i + 1)
            curr.pop()


if __name__ == "__main__":
    res = Solution().subsetsWithDup([1, 2, 2])
    print(res)
