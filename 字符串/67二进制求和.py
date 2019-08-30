#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


def addBinary(a: str, b: str) -> str:
    list_a = list(a)
    list_b = list(b)

    length = max(len(list_a), len(list_b))
    carry = 0
    res = []

    for i in range(1, length+1):
        num_a = 0
        if i <= len(list_a):
            num_a = int(list_a[-i])
        num_b = 0
        if i <= len(list_b):
            num_b = int(list_b[-i])

        num = num_a + num_b + carry
        if num // 2:
            num = num % 2
            carry = 1
        else:
            carry = 0
        res.insert(0, num)

    if carry:
        res.insert(0, 1)

    str_res = ''
    for s in res:
        str_res += str(s)

    return str_res

print(addBinary('11', '1'))


