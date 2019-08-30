#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


# def removeElement(nums: [int], val: int) -> int:
#     k = 0
#     for i, num in enumerate(nums):
#         if num != val:
#             nums[k] = num
#             k += 1
#         print(k)
#         print(nums)
#     print(nums[:k])
#     return k


def removeElement(nums: [int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)


removeElement([0,1,2,2,3,0,4,2], 2)
