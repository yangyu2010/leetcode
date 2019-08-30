#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


def pivotIndex(nums: [int]) -> int:
    total = sum(nums)

    left_total = 0
    for i, num in enumerate(nums):
        # if left_total * 2 + num == total:
        if left_total == (total - num) / 2:
            return i
        left_total += num
    return -1


# def pivotIndex(nums: [int]) -> int:
#     total = sum(nums)
#     part_sum = 0
#     for i, v in enumerate(nums):
#         if part_sum == (total - v) / 2:
#             return i
#         part_sum += v
#     return -1

# nums = [1, 7, 3, 6, 5, 6]
# 28
nums = [1, 2, 3]
print(pivotIndex(nums))