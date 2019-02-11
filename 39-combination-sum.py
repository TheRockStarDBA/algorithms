""" ##String # Backtracking
Related: Letter Combinations of a Phone Number - Medium
        Combination Sum II - Medium
        Combinations - Medium
        Combination Sum III - Medium
        Factor Combinations - Medium
        Combination Sum IV - Medium

Given a set of candidate numbers (candidates) (without duplicates) and a target 
number (target), find all unique combinations in candidates where the candidate 
numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
 [7],
 [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
 [2,2,2,2],
 [2,3,3],
 [3,5]
] """


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates = [i for i in candidates if i <= target]
        candidates.sort()
        result = []
        self.combination(candidates, target, result, [])
        return result

    def combination(self, candidates, target, result, current):
        s = sum(current) if current else 0
        if s > target:
            return
        elif s == target:
            result.append(current)
            return

        else:
            for i, v in enumerate(candidates):
                self.combination(candidates[i:], target, result, current + [v])


if __name__ == "__main__":
    candidates = [2, 3, 5]
    target = 8
    result = Solution().combinationSum(candidates, target)
    print(result)
