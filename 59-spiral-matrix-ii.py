""" 59. Spiral Matrix II - Medium
topic: array
related: 54. Spiral Matrix - Medium

Given a positive integer n, generate a square matrix filled with elements from 1
to n^2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
] """


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        num = 1
        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                matrix[top][j] = num
                num += 1
            for i in range(top + 1, bottom):
                matrix[i][right] = num
                num += 1
            for j in reversed(range(left, right + 1)):
                if top < bottom:
                    matrix[bottom][j] = num
                    num += 1
            for i in reversed(range(top + 1, bottom)):
                if left < right:
                    matrix[i][left] = num
                    num += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return matrix


if __name__ == "__main__":
    matrix = Solution().generateMatrix(3)
    print(matrix)
