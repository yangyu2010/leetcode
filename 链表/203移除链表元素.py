#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        curr = head

        while curr:
            print(curr.val)
            if curr.val == val:
                if prev:
                    prev.next = curr.next
                    # prev = curr
                else:
                    head = curr.next
                    prev = None
            else:
                prev = curr
            curr = curr.next

        return head

l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(2)
l4 = ListNode(1)
l5 = ListNode(4)
l6 = ListNode(5)
l7 = ListNode(6)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7

head = Solution().removeElements(l1, 5)
print('----------')
while head:
    print(head.val)
    head = head.next


