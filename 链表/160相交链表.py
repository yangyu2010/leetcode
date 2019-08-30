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


def getIntersectionNode(headA: ListNode, headB: ListNode):

    # 找到最后一个
    lastA = headA
    while lastA.next:
        lastA = lastA.next

    # 把b的首部 链接到a的尾部
    lastA.next = headB

    intersect = getIntersect(headA)
    if not intersect:
        return None

    ptr1 = headA
    ptr2 = intersect
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    lastA.next = None
    return ptr1





l1 = ListNode(2)
l2 = ListNode(6)

l3 = ListNode(4)
# l4 = ListNode(4)
# l5 = ListNode(5)

l6 = ListNode(1)
l7 = ListNode(5)
# l8 = ListNode(8)


l1.next = l2
l2.next = l3
# l3.next = l4
# l4.next = l5

l6.next = l7
# l7.next = l8
# l8.next = l3


# l5.next = l6
# l6.next = l7
# l7.next = l8

print(getIntersectionNode(l1, l6))







