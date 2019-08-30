#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


# class Solution:
#     def oddEvenList(self, head: ListNode) -> ListNode:
#         if not head:
#             return None
#
#         odd = head
#         even = head.next
#         even_start = even
#
#         while even and even.next:
#             odd.next = even.next
#             odd = even.next
#
#             even.next = odd.next
#             even = odd.next
#
#         odd.next = even_start
#         return head



l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7


head = Solution().oddEvenList(l1)
print('----------')
while head:
    print(head.val)
    head = head.next

