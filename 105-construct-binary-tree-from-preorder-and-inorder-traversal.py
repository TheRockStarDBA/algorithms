""" 105. Construct Binary Tree from Preorder and Inorder Traversal - Medium
#array #tree #depth-first search

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7 """


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        preorder_iter = iter(preorder)
        inorder_lookup = {n: i for i, n in enumerate(inorder)}

        def buildTreeHelper(start, end):
            if start > end:
                return None
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            root_idx = inorder_lookup[root_val]
            root.left = buildTreeHelper(start, root_idx - 1)
            root.right = buildTreeHelper(root_idx + 1, end)
            return root

        return buildTreeHelper(0, len(inorder) - 1)
