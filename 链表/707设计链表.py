#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class MyLink:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyLinkedList:
    head: MyLink

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.head:
            self.head = MyLink(val)
        else:
            temp = self.head
            self.head = MyLink(val)
            self.head.next = temp

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = self.head
        last = node
        while node:
            last = node
            node = node.next
        last.next = MyLink(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            temp = self.head
            self.head = MyLink(val)
            self.head.next = temp
        else:
            for i in range(index):
                print(i)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

# param_1 = obj.get(index)
obj.addAtHead(10)
obj.addAtTail(11)
obj.addAtIndex(1, 12)



# obj.deleteAtIndex(index)