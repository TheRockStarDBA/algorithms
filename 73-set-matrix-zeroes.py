""" 73. Set Matrix Zeroes - Medium

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution? """

# Approach 1: Additional Memory Approach

# Intuition
# If any cell of the matrix has a zero we can record its row and column number.
# All the cells of this recorded row and column can be marked zero in the next
# iteration.

# Algorithm
# We make a pass over our original array and look for zero entries.

# If we find that an entry at [i, j] is 0, then we need to record somewhere the
# row i and column j.

# So, we use two sets, one for the rows and one for the columns.

#  if matrix[i][j] == 0:
#      row_set.add(i)
#      column_set.add(j)

# Finally, we iterate over the original matrix. For every cell we check if the row
#  r or column c had been marked earlier. If any of them was marked, we set the
#  value in the cell to 0.

#  if r in row_set or c in column_set:
#      matrix[r][c] = 0

# Complexity Analysis
# Time Complexity: O(M×N) where M and N are the number of rows and columns respectively.
# Space Complexity: O(M+N).


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        nrows = len(matrix)
        ncols = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets,
        # update the elements
        for i in range(nrows):
            for j in range(ncols):
                if i in rows or j in cols:
                    matrix[i][j] = 0


# Approach 2: Brute O(1) space.

# Intuition
# In the above approach we use additional memory to keep a track of rows and
# columns which need to be set to zero. This additional use of space can be
# avoided by manipulating the original array instead.

# Algorithm
# Iterate over the original array and if we find an entry, say cell[i][j] to be 0,
# then we iterate over row i and column j separately and set all the non zero
# elements to some high negative dummy value (say -1000000). Note, choosing the
# right dummy value for your solution is dependent on the constraints of the
# problem. Any value outside the range of permissible values in the matrix will
# work as a dummy value. Finally, we iterate over the original matrix and if we
# find an entry to be equal to the high negative value (constant defined initially
#  in the code as MODIFIED), then we set the value in the cell to 0.

# Complexity Analysis

# Time Complexity : O((M×N)×(M+N)) where M and N are the number of rows and
# columns respectively. Even though this solution avoids using space, but is
# very inefficient since in worst case for every cell we might have to zero out
# its corresponding row and column. Thus for all (M×N) cells zeroing out (M + N)
# cells.
# Space Complexity : O(1)


class Solution2(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        dummy = -1000000
        nrows = len(matrix)
        ncols = len(matrix[0])
        for r in range(nrows):
            for c in range(ncols):
                if matrix[r][c] == 0:
                    # We modify the elements in place. Note, we only change the
                    # non zeros to dummy
                    for k in range(ncols):
                        matrix[r][k] = dummy if matrix[r][k] != 0 else 0
                    for k in range(nrows):
                        matrix[k][c] = dummy if matrix[k][c] != 0 else 0
        for r in range(nrows):
            for c in range(ncols):
                # Make a second pass and change all dummy elements to 0 """
                if matrix[r][c] == dummy:
                    matrix[r][c] = 0


# Approach 3: O(1) Space, Efficient Solution

# Intuition
# The inefficiency in the second approach is that we might be repeatedly setting
# a row or column even if it was set to zero already. We can avoid this by
# postponing the step of setting a row or a column to zeroes.

# We can rather use the first cell of every row and column as a flag. This flag
# would determine whether a row or column has been set to zero. This means for
# every cell instead of going to M+N cells and setting it to zero we just set
#  the flag in two cells.

# if matrix[i][j] == 0 :
#     matrix[i][0] = 0
#     matrix[0][j] = 0

# These flags are used later to update the matrix. If the first cell of a row is
#  set to zero this means the row should be marked zero. If the first cell of a
# column is set to zero this means the column should be marked zero.

# Algorithm
# We iterate over the matrix and we mark the first cell of a row i and first
# cell of a column j, if the condition in the pseudo code above is satisfied.
# i.e. if matrix[i][j] == 0.

# The first cell of row and column for the first row and first column is the
# same i.e. matrix[0][0]. Hence, we use an additional variable to tell us if the
# first column had been marked or not and the matrix[0][0] would be used to tell
# the same for the first row.

# Now, we iterate over the original matrix starting from second row and second
# column i.e. matrix[1][1] onwards. For every cell we check if the row r or
# column c had been marked earlier by checking the respective first row cell or
# first column cell. If any of them was marked, we set the value in the cell to 0.
# Note the first row and first column serve as the row_set and column_set that
# we used in the first approach.

# We then check if matrix [0][0] == 0, if this is the case, we mark the first row as zero.

# And finally, we check if the first column was marked, we make all entries in it as zeros.

# Complexity Analysis

# Time Complexity : O(M×N)
# Space Complexity : O(1)

from functools import reduce


class Solution3(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        first_col = reduce(lambda acc, i: acc or matrix[i][0] == 0,
                           range(len(matrix)), False)
        first_row = reduce(lambda acc, j: acc or matrix[0][j] == 0,
                           range(len(matrix[0])), False)

        m = len(matrix)
        n = len(matrix[0])

        # If an element is zero, we set the first element of the corresponding
        # row and column to 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # Iterate over the array once again and using the first row and first
        # column, update the elements.
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # See if the first row needs to be set to zero as well
        if first_row:
            for j in range(n):
                matrix[0][j] = 0

        # See if the first column needs to be set to zero as well
        if first_col:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    matrix3 = [[1, 0, 2, 3], [3, 4, 0, 2], [1, 3, 1, 5]]

    Solution().setZeroes(matrix)
    Solution2().setZeroes(matrix2)
    Solution3().setZeroes(matrix3)
    print(matrix)
    print(matrix2)
    print(matrix3)
