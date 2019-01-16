""" 83. Remove Duplicates from Sorted List

Topic: Linked list (Easy)

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3 """

# Approach: Straight-Forward Approach
# Algorithm

# This is a simple problem that merely tests our ability to manipulate list node pointers.
# Because the input list is sorted, we can determine if a node is a duplicate by comparing
# its value to the node after it in the list. If it is a duplicate, we change the next pointer
# of the current node so that it skips the next node and points directly to the one after the next node.

# Complexity Analysis

# Time complexity : O(n). Because each node in the list is checked exactly once to determine if it is a duplicate or not, the total run time is O(n), where n is the number of nodes in the list.

# Space complexity : O(1). No additional space is used.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(2)
    n1.next = n2
    n2.next = n3
    result = Solution().deleteDuplicates(n1)
    current = result
    while current is not None:
        print(current.val)
        current = current.next
