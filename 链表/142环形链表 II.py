#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

def getIntersect(head: ListNode):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return slow
    return None


def detectCycle(head: ListNode):
    intersect = getIntersect(head)
    if not intersect:
        return None

    ptr1 = head
    ptr2 = intersect
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    return ptr1


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

l5.next = l3

print(detectCycle(l1).val)