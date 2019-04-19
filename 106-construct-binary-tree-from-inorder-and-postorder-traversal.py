""" 106. Construct Binary Tree from Inorder and Postorder Traversal - Medium
#array #tree #depth first search

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
 """


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        inorder_lookup = {n: i for i, n in enumerate(inorder)}

        def buildTreeHelper(start, end):
            if start < end:
                root_val = postorder.pop()
                root = TreeNode(root_val)
                root_idx = inorder_lookup[root_val]
                root.right = buildTreeHelper(root_idx + 1, end)
                root.left = buildTreeHelper(start, root_idx)
                return root

        return buildTreeHelper(0, len(inorder))
