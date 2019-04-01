""" 100. Same Tree - Easy
# tree, depth-first search

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and
the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false """


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Approach 1: Recursion
# Intuition
# The simplest strategy here is to use recursion. Check if p and q nodes are not
# None, and their values are equal. If all checks are OK, do the same for the
# child nodes recursively.

# Time:  O(n)
# Space: O(log(n)) in the best case of completely balanced tree and O(n) in the
# worst case of completely unbalanced tree, to keep a recursion stack.


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(
            p.left, q.left)


# Approach 2: Iteration
# Intuition

# Start from the root and then at each iteration pop the current node out of the
# deque. Then do the same checks as in the approach 1 :

# p and p are not None,

# p.val is equal to q.val,

# and if checks are OK, push the child nodes.

from collections import deque


class Solution2(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True

        deq = deque([
            (p, q),
        ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True