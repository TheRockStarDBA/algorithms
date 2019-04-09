""" 109. Convert Sorted List to Binary Search Tree -Medium
#tree #depth-first search

Given a singly linked list where elements are sorted in ascending order, convert 
it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height 
balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5 """

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Approach 1: Recursion + Conversion to Array

class Solution(object):

    # Convert the given linked list to an array
    def mapListToValues(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # Form an array out of the given linked list and then use the array to
        # form the BST.
        values = self.mapListToValues(head)

        def convertListToBST(left, right):
            # left and right represent the start and end of the given array
            if left > right:
                return None

            mid = (left+right)//2
            node = TreeNode(values[mid])

            # Base case for when there is only one element left in the array
            if left == right:
                return node

            # Recursively form BST on the two halves
            node.left = convertListToBST(left, mid-1)
            node.right = convertListToBST(mid+1, right)
            return node

        return convertListToBST(0, len(values)-1)
