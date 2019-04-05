""" 148. Sort List - Medium
# linked list, sort

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5 """


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head


if __name__ == "__main__":
    n1 = ListNode(4)
    n2 = ListNode(2)
    n3 = ListNode(1)
    n4 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
