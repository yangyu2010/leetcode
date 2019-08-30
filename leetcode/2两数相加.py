#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    node = ListNode(0)
    node_temp = node
    while (l1 or l2 or carry):
        # num1 = 0
        # if l1.val:
        #     num1 = l1.val
        # num2 = 0
        # if l2.val:
        #     num2 = l2.val
        num1 = l1.val if l1 else 0
        num2 = l2.val if l2 else 0

        total = num1 + num2 + carry
        carry = total // 10
        rem = total % 10
        # print(rem)

        node1 = ListNode(rem)
        node_temp.next = node1
        node_temp = node1

        l1 = l1.next if l1 else 0
        l2 = l2.next if l2 else 0

    return node.next

# def addTwoNumbers(l1: [int], l2: [int]) -> [int]:
#     print(l1)
#     print(l2)
#
#

# [2,4,3]
# [5,6,4]


a1 = ListNode(0)
# a2 = ListNode(1)
# a3 = ListNode(5)
# a1.next = a2
# a2.next = a3

b1 = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

list = addTwoNumbers(a1, b1)

print("-----------")
# print(list)
while list.next:
    print(list.val)
    list = list.next
else:
    print(list.val)