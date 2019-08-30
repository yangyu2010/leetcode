#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyHashSet:
    default_initial_capacity = 1 << 4

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = [None] * self.default_initial_capacity

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        index = self.__getIndex__(key)
        node = self.list[index]
        if not node:
            self.list[index] = ListNode(key)
        else:
            while node.next:
                node = node.next
            node.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = self.__getIndex__(key)
        node = self.list[index]
        prev = None
        while node:
            if node.val == key:
                # 是该链表的第一个 可能后面还有
                if not prev:
                    if node.next:
                        self.list[index] = node.next
                    else:
                        self.list[index] = None
                else:
                    prev.next = node.next
                return
            prev = node
            node = node.next

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = self.__getIndex__(key)
        node = self.list[index]
        while node:
            if node.val == key:
                return True
            node = node.next
        return False

    def __getIndex__(self, key: int):
        return key % self.default_initial_capacity


# hashSet.add(1)
# hashSet.add(9)
# print(hashSet.contains(9))
# print(hashSet.contains(1))
# hashSet.remove(9)
# print(hashSet.contains(9))
# print(hashSet.contains(1))


# hashSet.add(1)
# hashSet.add(2)
# print(hashSet.contains(1))    #// 返回 true
# print(hashSet.contains(3))    #// 返回 false (未找到)
# hashSet.add(2)
# print(hashSet.contains(2))    #// 返回 true
# hashSet.remove(2)
# print(hashSet.contains(2))    #// 返回  false (已经被删除)
