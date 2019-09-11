#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class MyCircularQueue:
    # -1默认位置
    head = -1
    tail = -1

    def __init__(self, length: int):
        self.length = length
        self.queue = [None] * length

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.length
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.queue[self.head] = None
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.length
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.head == -1:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.tail == -1:
            return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.head == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return (self.tail + 1) % self.length == self.head


obj = MyCircularQueue(3)
obj.enQueue(1)
obj.enQueue(2)
obj.enQueue(3)
obj.enQueue(4)
print(obj.deQueue())
print(obj.deQueue())

obj.enQueue(3)
obj.enQueue(4)

print(obj.deQueue())

print(obj.queue)
print(obj.head)
print(obj.tail)

print(obj.deQueue())

# print(obj.deQueue())
# print(obj.deQueue())
# obj.enQueue(2)
# obj.enQueue(3)
# obj.enQueue(4)
#
# print(obj.queue)
# print(obj.Rear())
# print(obj.isFull())
# print(obj.deQueue())
# print(obj.queue)
#
# print(obj.head)
# print(obj.tail)

# obj.deQueue()
# obj.enQueue(4)
# obj.Rear()

# obj = MyCircularQueue(5)
# # print(obj.queue)
# # print(len(obj.queue))
#
# obj.enQueue(1)
# obj.enQueue(2)
# obj.enQueue(3)
# obj.enQueue(4)
# obj.enQueue(5)
# # print(obj.enQueue(6))
#
# print(obj.deQueue())
# print(obj.deQueue())
# # print(obj.deQueue())
# # print(obj.deQueue())
# # print(obj.deQueue())
#
# print(obj.enQueue(6))
# print(obj.enQueue(7))
#
# print(obj.head)
# print(obj.tail)
#
# # print(obj.deQueue())
# # print(obj.deQueue())
# # print(obj.deQueue())
# # print(obj.deQueue())
# print(obj.isEmpty())
# print(obj.isFull())
#
#
# # print(obj.enQueue(6))
#
# print(obj.queue)
