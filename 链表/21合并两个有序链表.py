#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None


# 递归
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

# #迭代
# class Solution:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         prehead = ListNode(-1)
#         prev = prehead
#         while l1 and l2:
#             if l1.val < l2.val:
#                 prev.next = l1
#                 l1 = l1.next
#             else:
#                 prev.next = l2
#                 l2 = l2.next
#             prev = prev.next
#
#         prev.next = l1 if l1 else l2
#
#         return prehead.next



l1 = ListNode(1)
l2 = ListNode(12)
l3 = ListNode(13)
l4 = ListNode(14)

l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(17)
l8 = ListNode(88)


l1.next = l2
l2.next = l3
l3.next = l4
# l4.next = l5

l5.next = l6
l6.next = l7
l7.next = l8
# l8.next = l3



head = Solution().mergeTwoLists(l1, l5)
print('----------')
while head:
    print(head.val)
    head = head.next
