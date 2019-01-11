#TOPIC: ARRAY; BACKTRACKING;
#Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
#Each number in candidates may only be used once in the combination.
#
#Note:
#
#All numbers (including target) will be positive integers.
#The solution set must not contain duplicate combinations.
#Example 1:
#
#Input: candidates = [10,1,2,7,6,1,5], target = 8,
#A solution set is:
#[
#  [1, 7],
#  [1, 2, 5],
#  [2, 6],
#  [1, 1, 6]
#]
#Example 2:
#
#Input: candidates = [2,5,2,1,2], target = 5,
#A solution set is:
#[
#  [1,2,2],
#  [5]
#]

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        candidates = [i for i in candidates if i<=target]
        result = []
        self.combination(candidates, target, result, [])
        return result

    def combination(self, candidates, target, result, current):
        s = sum(current) if current else 0
        if s>target:
            return
        elif s==target:
            result.append(current)
            return
        else:
            for i,v in enumerate(candidates):
                if i>0 and candidates[i-1]==candidates[i]:
                    continue
                self.combination(candidates[i+1:], target, result, current+[v])

Solution().combinationSum2(candidates = [2,5,2,1,2], target = 5)
Solution().combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
