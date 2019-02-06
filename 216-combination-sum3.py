""" Find all possible combinations of k numbers that add up to a number n, given
that only numbers from 1 to 9 can be used and each combination should be a unique
set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
 """


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        nums = [i for i in range(1, 10)]
        self.combination(k, n, nums, result, [])
        return result

    def combination(self, k, n, nums, result, current):
        s = sum(current) if current else 0
        if s > n:
            return
        elif s == n and len(current) == k:
            result.append(current)
            return

        else:
            for i, v in enumerate(nums):
                if len(current) >= k:
                    continue
                self.combination(k, n, nums[i + 1:], result, current + [v])


if __name__ == "__main__":
    print(Solution().combinationSum3(k=3, n=9))
    print(Solution().combinationSum3(k=3, n=10))
