#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

# 快慢指针
# def hasCycle(head: ListNode):
#     fast = head
#     slow = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#         print(slow.val)
#         print(fast.val)
#
#         if slow == fast:
#             return True
#     return False


# 哈希表
def hasCycle(head: ListNode):
    ''''''

    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        print(slow.val)
        print(fast.val)
        print('--------')
        if slow == fast:
            return True
    return False


    # if not head:
    #     return False
    # hash_table = set()
    # temp = head
    #
    # while temp:
    #     if temp in hash_table:
    #         return True
    #     else:
    #         hash_table.add(temp)
    #         temp = temp.next
    # return False


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

print(hasCycle(l1))


# l1 = ListNode(4)
# l2 = ListNode(1)
# l3 = ListNode(8)
# l4 = ListNode(4)
# l5 = ListNode(5)
#
# l6 = ListNode(5)
# l7 = ListNode(0)
# l8 = ListNode(1)
#
#
# l1.next = l2
# l2.next = l3
# l3.next = l4
# l4.next = l5
#
#
# l6.next = l7
# l7.next = l8
# l8.next = l3
#
# l5.next = l6

print(hasCycle(l1))
