""" 23. Merge k Sorted Lists

Topics: linked list, divide and conquer, heap (Hard)
Related: Merge Two Sorted Lists - Easy
Ugly Number II - Medium

Merge k sorted linked lists and return it as one sorted list. Analyze and describe
its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6 """


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.next)


# Approach 1: Merge with Divide And Conquer
# Intuition & Algorithm
# Pair up k lists and merge each pair.
# After the first pairing, k lists are merged into k/2 lists with average 2N/k
# length, then k/4, k/8 and so on.
# Repeat this procedure until we get the final sorted linked list.
# Thus, we'll traverse almost N nodes per pairing and merging, and repeat this
# procedure about log(2)k times.
# Time complexity : O(N log k), where k is the number of linked lists.
# Space complexity : O(1)
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k = len(lists)
        interval = 1
        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if k > 0 else lists

    def merge2Lists(self, l1, l2):
        dummy = current = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l1
                l1 = current.next.next
            current = current.next
        if not l1:
            current.next = l2
        else:
            current.next = l1
        return dummy.next


# Approach 2: Merge with heap quene optimization
# Compare every k nodes (head of every linked list) and get the node with the
# smallest value.
# Extend the final sorted linked list with the selected nodes.
# Time:  O(nlogk)
# Space: O(k)

import heapq


class Solution2(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current = dummy

        heap = []
        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, sorted_list))

        while heap:
            # Pop and return the smallest item from the heap, maintaining the heap invariant.
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))

        return dummy.next


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n4 = ListNode(1)
    n5 = ListNode(3)
    n6 = ListNode(4)
    n4.next = n5
    n5.next = n6
    n7 = ListNode(2)
    n8 = ListNode(6)
    n7.next = n8
    result = Solution().mergeKLists([n1, n4, n7])
    print(result)
