# -*- coding: utf-8 -*-

'''
@Author: YangYu
@Github: https://github.com/yangyu2010
@Date: 2019-09-02 09:24:18
@LastEditors: YangYu
@LastEditTime: 2019-09-03 16:17:50
'''

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
