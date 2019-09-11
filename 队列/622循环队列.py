#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class MyCircularQueue:

    # p_start = 0
    # p_end = 0
    # length = 0

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = []
        self.length = k - 1 if k > 0 else 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if len(self.queue) > self.length:
            return False
        self.queue.append(value)
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.queue.pop(0)
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[0]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return len(self.queue) == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return len(self.queue) > self.length


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(8)
obj.enQueue(3)
obj.enQueue(9)
obj.enQueue(5)
obj.enQueue(0)
# print(obj.queue)
obj.deQueue()
obj.deQueue()

print(obj.queue)