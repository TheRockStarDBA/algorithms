""" 129. Sum Root to Leaf Numbers - Medium
#tree #depth first search

Given a binary tree containing digits from 0-9 only, each root-to-leaf path could
represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 """


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursive
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumNumbersHelper(root, 0)

    def sumNumbersHelper(self, node, s):
        if not node:
            return 0
        if not node.left and not node.right:
            return s * 10 + node.val
        return self.sumNumbersHelper( node.left, s * 10 + node.val) + \
            self.sumNumbersHelper(node.right, s * 10 + node.val)


# depth first search
class Solution2(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        stack = [(root, root.val)]
        result = 0
        while stack:
            node, value = stack.pop()
            if not node.left and not node.right:
                result += value
            if node.left:
                stack.append((node.left, value * 10 + node.left.val))
            if node.right:
                stack.append((node.right, value * 10 + node.right.val))
        return result