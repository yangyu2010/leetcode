#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


def plusOne(digits: [int]) -> [int]:
    carry = 1
    nums = []

    for i in range(len(digits) - 1, -1, -1):
        num = digits[i]
        if num + carry >= 10:
            nums.append(0)
            carry = 1
        else:
            if carry:
                nums.insert(0, num + 1)
            else:
                nums.insert(0, num)
            carry = 0
    if carry == 1:
        nums.insert(0, 1)
    return nums


# nums = [4, 3, 2, 1]
# nums = [1, 9, 9]
nums = [4, 0, 9]
print(plusOne(nums))


