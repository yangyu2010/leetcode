#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        preHead = head
        total = 1

        old_tail = head
        while old_tail.next:
            old_tail = old_tail.next
            total += 1

        old_tail.next = preHead

        cur = 0
        while preHead:
            if cur == (total - k % total - 1):
                temp = preHead.next
                preHead.next = None
                return temp
            preHead = preHead.next
            cur += 1

        return None


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

# l6 = ListNode(6)
# l7 = ListNode(7)
# l8 = ListNode(8)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
# l5.next = l6
# l6.next = l7
# l7.next = l8


head = Solution().rotateRight(l1, 1)
print('----------')
while head:
    print(head.val)
    head = head.next

