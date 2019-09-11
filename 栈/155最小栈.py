#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.help = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.help or x <= self.help[-1]:
            self.help.append(x)

    def pop(self) -> None:
        if self.stack[-1] == self.help[-1]:
            self.help.pop()
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        if self.help:
            return self.help[-1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.getMin())
print(obj.top())
print(obj.help)

obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())

obj.pop()
print(obj.top())
print(obj.getMin())
