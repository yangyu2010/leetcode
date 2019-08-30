#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang

class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        preHead = ListNode(0)
        prev = preHead
        carry = 0

        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            total = num1 + num2 + carry

            carry = total // 10
            rem = total % 10
            prev.next = ListNode(rem)

            prev = prev.next
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0

        return preHead.next


l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(3)

l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l8 = ListNode(8)


l1.next = l2
l2.next = l3
l3.next = l4
# l4.next = l5

l5.next = l6
l6.next = l7
l7.next = l8
# l8.next = l3



head = Solution().addTwoNumbers(l1, l5)
print('----------')
while head:
    print(head.val)
    head = head.next