""" 86. Partition List - Medium
Topic: two-pointers

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
 """

# Approach: Two Pointer Approach
# Intuition

# We can take two pointers before and after to keep track of the two linked lists
# as described above. These two pointers could be used two create two separate
# lists and then these lists could be combined to form the desired reformed list.

# Complexity Analysis

# Time Complexity: O(N), where N is the number of nodes in the original linked
# list and we iterate the original list.
# Space Complexity: O(1), we have not utilized any extra space, the point to note
# is that we are reforming the original list, by moving the original nodes, we
# have not used any extra space as such.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # before and after are the two pointers used to create two list
        # dummy_before and dummy_after are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        dummy_before, dummy_after = ListNode(-1), ListNode(-1)
        before, after = dummy_before, dummy_after

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        # Last node of "after" list would also be ending node of the reformed list
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = dummy_after.next

        return dummy_before.next


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(3)
    n4 = ListNode(2)
    n5 = ListNode(5)
    n6 = ListNode(2)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    result = Solution().partition(n1, 3)
    print(result)
