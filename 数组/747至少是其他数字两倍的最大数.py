#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang

'''
    找到最大数和第二个大的数字比较
'''
# def dominantIndex(nums: [int]) -> int:
#     maxNum1 = 0
#     maxNum2 = 0
#     index = 0
#
#     for i, num in enumerate(nums):
#         if num > maxNum1:
#             if maxNum1 > maxNum2:
#                 maxNum2 = maxNum1
#             maxNum1 = num
#             index = i
#         elif num > maxNum2:
#             maxNum2 = num
#     if maxNum1 >= maxNum2 * 2:
#         return index
#     return -1


def dominantIndex(nums: [int]) -> int:
    nums_max = max(nums)
    index = 0
    for i in range(len(nums)):
        if nums[i] == nums_max:
            index = i
        elif nums[i] * 2 > nums_max:
            return -1
    # for i, num in enumerate(nums):
    #     if num == nums_max:
    #         index = i
    #     elif num * 2 > nums_max:
    #         return -1
    return index


# nums = [3, 6, 4, 1, 0]
nums = [1, 2, 3, 3, 8]
print(dominantIndex(nums))