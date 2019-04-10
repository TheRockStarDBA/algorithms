""" 156. Binary Tree Upside Down - Medium

* Given a binary tree where all the right nodes are either leaf nodes with
* a sibling (a left node that shares the same parent node) or empty,
*
* Flip it upside down and turn it into a tree where the original right nodes turned
* into left leaf nodes.
* Return the new root.
*
* For example:
* Given a binary tree {1,2,3,4,5},
*     1
*    / \
*   2   3
*  / \
* 4   5
* return the root of the binary tree [4,5,2,#,#,3,1].
*    4
*   / \
*  5   2
*     / \
*    3   1
*


 """


# Definition for binary tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """