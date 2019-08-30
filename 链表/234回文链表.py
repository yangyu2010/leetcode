#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        prev = None
        while slow:
            # slow.next, prev, slow = prev, slow, slow.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        while head != mid:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True



l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(2)
l5 = ListNode(1)
# l6 = ListNode(6)
# l7 = ListNode(7)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
# l5.next = l6
# l6.next = l7


head = Solution().isPalindrome(l1)
# print('----------')
print(head)
