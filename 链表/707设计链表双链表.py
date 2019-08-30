#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    head = None
    tail = None

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0:
            return -1
        if index == 0:
            return self.head.val if self.head else -1
        temp = self.head
        cur = 0
        while temp:
            if cur == index:
                return temp.val
            temp = temp.next
            cur += 1
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.head:
            temp = ListNode(val)
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        else:
            self.head = ListNode(val)
            self.tail = self.head

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.tail:
            temp = ListNode(val)
            self.tail.next = temp
            self.tail = temp
        else:
            self.tail = ListNode(val)
            self.head = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # 小于等于0时 默认插头部
        if index <= 0:
            self.addAtHead(val)
            return

        cur = 0
        prev = self.head
        while prev:
            if cur == index - 1:
                break
            else:
                prev = prev.next
                cur += 1

        if cur != index - 1 or not prev:
            return None

        temp = ListNode(val)
        next = prev.next
        prev.next = temp
        temp.next = next

        if prev == self.tail:
            self.tail = temp


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            return None
        if index == 0:
            if self.head:
                self.head = self.head.next
            return None

        cur = 0
        prev = self.head
        while prev:
            if cur == index - 1:
                break
            else:
                prev = prev.next
                cur += 1

        if cur != index - 1 or not prev:
            return None

        # 如果前一个是 当前的最后一个 代表越界了
        if prev == self.tail:
            return None

        next = prev.next.next
        prev.next = next
        if next:
            next.prev = prev
        else:
            self.tail = prev


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(0)
# print(param_1)

obj.addAtHead(1)
obj.addAtHead(2)

obj.addAtTail(3)
# obj.addAtHead(2)
# obj.addAtTail(4)

# 2134

# obj.addAtIndex(1, 10)
# obj.addAtIndex(4, 10)
obj.deleteAtIndex(2)


print(obj.head.val)
print(obj.tail.val)

# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


print('-----------')
temp = obj.head
while temp:
    print(temp.val)
    temp = temp.next
