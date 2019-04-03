""" 101. Symmetric Tree - Easy
# tree, depth-first search, breadth-first search

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around
its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively. """

# Approach 1: Recursive
# A tree is symmetric if the left subtree is a mirror reflection of the right subtree.
# Therefore, the question is: when are two trees a mirror reflection of each other?

# Two trees are a mirror reflection of each other if:
# Their two roots have the same value.
# The right subtree of each tree is a mirror reflection of the left subtree of
# the other tree.

# This is like a person looking at a mirror. The reflection in the mirror has the
# same head, but the reflection's right arm corresponds to the actual person's
# left arm, and vice versa.

# Complexity Analysis：

# Time complexity : O(n). Because we traverse the entire input tree once, the
# total run time is O(n), where n is the total number of nodes in the tree.

# Space complexity : The number of recursive calls is bound by the height of the
# tree. In the worst case, the tree is linear and the height is in O(n).
# Therefore, space complexity due to recursive calls on the stack is O(n) in the
# worst case.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return (t1.val == t2.val) and self.isMirror(t1.left, t2.right) and \
            self.isMirror(t1.right, t2.left)


# Approach 2: Iterative
# Instead of recursion, we can also use iteration with the aid of a queue. Each two
# consecutive nodes in the queue should be equal, and their subtrees a mirror of
# each other. Initially, the queue contains root and root. Then the algorithm works
# similarly to BFS, with some key differences. Each time, two nodes are extracted
# and their values compared. Then, the right and left children of the two nodes are
# inserted in the queue in opposite order. The algorithm is done when either the
# queue is empty, or we detect that the tree is not symmetric (i.e. we pull out two
# consecutive nodes from the queue that are unequal).
class Solution2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        stack = []
        stack.append(root.left)
        stack.append(root.right)

        while stack:
            t1, t2 = stack.pop(), stack.pop()
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            stack.append(t1.left)
            stack.append(t2.right)
            stack.append(t1.right)
            stack.append(t2.left)

        return True

