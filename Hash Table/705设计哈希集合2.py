#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


from AVLTree import AVLTree


class MyHashSet:
    default_initial_capacity = 17

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = [None] * self.default_initial_capacity

    def add(self, key: int) -> None:
        if self.contains(key):
            return
        index = self.__getIndex__(key)
        tree = self.list[index]
        if not tree:
            tree = AVLTree()
            self.list[index] = tree
        tree.insert(key)

    def remove(self, key: int) -> None:
        index = self.__getIndex__(key)
        tree = self.list[index]
        if tree:
            tree.delete(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index = self.__getIndex__(key)
        tree = self.list[index]
        if tree:
            if tree.find(key):
                return True
        return False

    def __getIndex__(self, key: int):
        return key % self.default_initial_capacity


hashSet = MyHashSet()

# hashSet.add(1)
# hashSet.add(9)
# print(hashSet.contains(9))
# print(hashSet.contains(1))
# hashSet.remove(9)
# print(hashSet.contains(9))
# print(hashSet.contains(1))


hashSet.add(1)
hashSet.add(2)
print(hashSet.contains(1))    #// 返回 true
print(hashSet.contains(3))    #// 返回 false (未找到)
hashSet.add(2)
print(hashSet.contains(2))    #// 返回 true
hashSet.remove(2)
print(hashSet.contains(2))    #// 返回  false (已经被删除)
