#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang

'''
https://leetcode-cn.com/problems/reverse-linked-list/
'''

from ListNode import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev


# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         l = [1, 2, 3, 4]
#         l.reverse()
#         print(l)


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

head = Solution().reverseList(l1)

print('-----------')
while head:
    print(head.val)
    head = head.next