#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

    def __str__(self):
        s = ''
        if self.prev:
            s += str(self.prev.val)
        else:
            s += 'none'

        s += ('->%d->' % self.val)

        if self.next:
            s += str(self.next.val)
        else:
            s += 'none'
        return s
