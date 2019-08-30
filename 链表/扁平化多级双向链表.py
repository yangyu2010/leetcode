#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class ListNode:
    def __init__(self, val, child):
        self.val = val
        self.prev = None
        self.next = None
        self.child = child


class Solution:
    def flatten(self, head: ListNode) -> ListNode:
        preHead = ListNode(-1, None)
        prev = preHead

        temp = head
        while temp:
            prev.next = temp

            temp_child = temp.child
            while temp_child:
                print(temp_child.val)
                prev.next = temp_child
                temp_child = temp_child.next


            temp = temp.next
            prev = prev.next

        return preHead.next





l1 = ListNode(1, None)
l2 = ListNode(1, None)
l3 = ListNode(2, None)
l4 = ListNode(3, None)

l5 = ListNode(5, None)
l6 = ListNode(6, None)
l7 = ListNode(7, None)
l8 = ListNode(8, None)


l1.next = l2
l2.next = l3
l3.next = l4


# l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8

l2.child = l5



head = Solution().flatten(l1)
print('----------')
while head:
    print(head.val)
    head = head.next