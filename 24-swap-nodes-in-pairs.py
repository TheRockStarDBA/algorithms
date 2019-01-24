""" 24. Swap Nodes in Pairs

Topic: linked list - Medium
Related: Reverse Nodes in k-Group - Hard

Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            p1 = current.next
            p2 = current.next.next
            current.next, p1.next, p2.next = p2, p2.next, p1
            current = current.next.next

        return dummy.next


if __name__ == "__main__":
    n0 = ListNode(1)
    n1 = ListNode(2)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n0.next = n1
    n1.next = n2
    n2.next = n3

    result = Solution().swapPairs(n0)
    print(result)
