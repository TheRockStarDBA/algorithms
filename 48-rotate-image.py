""" 48. Rotate Image
Topic: Array (Medium)

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
] """

# Complexity Analysis


# Time complexity : O(n^2) is a complexity given by two inserted loops.
# Space complexity : O(1) since we do a rotation in place and allocate only the
# list of 4 elements as a temporary helper.
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix[0])
        for i in range(n // 2):
            for j in range(i, n - 1 - i):
                temp = [0] * 4
                # store 4 elements in temp array
                for k in range(4):
                    temp[k] = matrix[i][j]
                    i, j = j, n - 1 - i
                # rotate 4 elements
                for k in range(4):
                    matrix[i][j] = temp[(k - 1) % 4]
                    i, j = j, n - 1 - i


if __name__ == "__main__":
    input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(input_matrix)
    print(input_matrix)
