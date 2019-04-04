""" 110. Balanced Binary Tree - Easy
#tree, depth-first search

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ 
by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

 """

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.getHeight(root) >= 0

    def getHeight(self, root):
        if not root:
            return 0
        left_height, right_height = self.getHeight(
            root.left), self.getHeight(root.right)
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1
