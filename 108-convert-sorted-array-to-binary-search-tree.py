""" 108. Convert Sorted Array to Binary Search Tree - Easy
#tree #depth-first search

Given an array where elements are sorted in ascending order, convert it to a height 
balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in 
which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height 
balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5 """


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def convertListToBST(left, right):
            # left and right represent the start and end of the given array
            if left > right:
                return None

            mid = (left+right)//2
            node = TreeNode(nums[mid])

            # Base case for when there is only one element left in the array
            if left == right:
                return node

            # Recursively form BST on the two halves
            node.left = convertListToBST(left, mid-1)
            node.right = convertListToBST(mid+1, right)
            return node

        return convertListToBST(0, len(nums)-1)
