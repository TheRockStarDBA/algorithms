""" 98. Validate Binary Search Tree - Medium
#tree, #depth-first search

Binary Tree Inorder Traversal - Medium
Find Mode in Binary Search Tree - Easy

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.

ref: https://leetcode.com/problems/validate-binary-search-tree/solution/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Approach 1: Inorder traversal

# Let's use the order of nodes in the inorder traversal Left -> Node -> Right.
# Left -> Node -> Right order of inorder traversal means for BST that each element
# should be smaller than the next one.

# Hence the algorithm with O(N) time complexity and O(N) space complexity could be simple:

# Compute inorder traversal list inorder.
# Check if each element in inorder is smaller than the next one.


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal is smaller than the previous
            # one that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True


# Approach 2: Recursion
# The idea above could be implemented as a recursion. One compares the node value
# with its upper and lower limits if they are available. Then one repeats the same
# step recursively for left and right subtrees.


class Solution2(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def isBSTHelper(node, lower_limit, upper_limit):
            if lower_limit is not None and node.val <= lower_limit:
                return False
            if upper_limit is not None and upper_limit <= node.val:
                return False

            left = isBSTHelper(node.left, lower_limit,
                               node.val) if node.left else True
            if left:
                right = isBSTHelper(node.right, node.val,
                                    upper_limit) if node.right else True
                return right
            else:
                return False

        return isBSTHelper(root, None, None)


# Approach 3: Iteration
# The above recursion could be converted into iteration, with the help of stack.
# DFS would be better than BFS since it works faster here.
class Solution3(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = [
            (root, None, None),
        ]
        while stack:
            root, lower_limit, upper_limit = stack.pop()
            if root.right:
                if root.right.val > root.val:
                    if upper_limit and root.right.val >= upper_limit:
                        return False
                    stack.append((root.right, root.val, upper_limit))
                else:
                    return False
            if root.left:
                if root.left.val < root.val:
                    if lower_limit and root.left.val <= lower_limit:
                        return False
                    stack.append((root.left, lower_limit, root.val))
                else:
                    return False
        return True