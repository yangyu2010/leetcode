#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n < 0:
            return head

        if n == 0:
            return head.next

        fast = head
        slow = head
        for i in range(n):
            if fast:
                fast = fast.next if fast.next else head
            else:
                print('超出界限')
                break
        # print(fast.val)

        if not fast:
            return None

        if fast == head:
            return head.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        # print(fast.val)
        # print(slow.val)
        slow.next = slow.next.next
        return head


# class Solution:
#     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#         pre = ListNode(0)
#         pre.next = head
#         start = pre
#         end = pre
#
#         while n != 0:
#             start = start.next
#             n -= 1
#
#         while not start.next:
#             start = start.next
#             end = end.next
#
#         end.next = end.next.next
#         return pre.next



l1 = ListNode(1)
l2 = ListNode(2)
# l3 = ListNode(3)
# l4 = ListNode(4)
# l5 = ListNode(5)

l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5

# print()

head = Solution().removeNthFromEnd(l1, 2)
while head:
    print(head.val)
    head = head.next

