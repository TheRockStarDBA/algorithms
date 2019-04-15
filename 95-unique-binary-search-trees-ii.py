""" 95. Unique Binary Search Trees II - Medium
#dynamic programming #tree

Given an integer n, generate all structurally unique BST's (binary search trees)
that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3 """


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        if self:
            serial = []
            queue = [self]

            while queue:
                cur = queue[0]

                if cur:
                    serial.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    serial.append("#")

                queue = queue[1:]

            while serial[-1] == "#":
                serial.pop()

            return repr(serial)

        else:
            return None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        return self.dfs(1, n)

    def dfs(self, start, end):
        result = []
        if start > end:
            result.append(None)
        for i in range(start, end + 1):
            left = self.dfs(start, i - 1)
            right = self.dfs(i + 1, end)
            for j in left:
                for k in right:
                    curr = TreeNode(i)
                    curr.left = j
                    curr.right = k
                    result.append(curr)
        return result


if __name__ == "__main__":
    result = Solution().generateTrees(n=3)
    print(result)
