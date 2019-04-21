""" 119. Pascal's Triangle II - Easy
#array

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space? """


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [0] * (rowIndex + 1)
        result[0] = 1
        for i in range(rowIndex):
            for j in range(i + 1, 0, -1):
                result[j] += result[j - 1]

        return result


if __name__ == "__main__":
    res = Solution().getRow(rowIndex=3)
    print(res)