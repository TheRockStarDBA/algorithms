""" 118. Pascal's Triangle - Easy
Topic: array, dynamic programming
Related:Pascal's Triangle II - Easy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
] """

# Approach: Dynamic Programming
# Intuition

# If we have the a row of Pascal's triangle, we can easily compute the next row
# by each pair of adjacent values.


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            triangle.append([])
            for j in range(i + 1):
                if j in (0, i):
                    triangle[i].append(1)
                else:
                    triangle[i].append(triangle[i - 1][j - 1] +
                                       triangle[i - 1][j])
        return triangle


class Solution2(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return []
        if numRows == 1: return [1]
        res = [[1], [1, 1]]

        def recursive_add(nums):
            res = nums[:1]
            for i in range(len(nums)):
                if i < len(nums) - 1:
                    res += [nums[i] + nums[i + 1]]
                res += nums[:1]
            return res

        while len(res) < numRows:
            res.extend([recursive_add(res[-1])])

        return res


if __name__ == "__main__":
    triangle = Solution().generate(5)
    triangle2 = Solution().generate(7)
    print(triangle)
    print(triangle2)