#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


# def findMaxConsecutiveOnes(nums: [int]) -> int:
#     res = 0
#     return_num = 0
#     check_num = 1
#     for i, num in enumerate(nums):
#         if check_num == num:
#             res += 1
#         else:
#             res = num
#             # if num == 0:
#             #     res = 0
#             # else:
#             #     res = 1
#         return_num = max(return_num, res)
#     return return_num


def findMaxConsecutiveOnes(nums: [int]) -> int:
    res = 0
    count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            if count > res:
                res = count
            count = 0
    return max(res, count)

print(findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
print(findMaxConsecutiveOnes([0]))

