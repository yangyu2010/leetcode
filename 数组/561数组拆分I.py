#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


# class Solution:
#     def arrayPairSum(self, nums: [int]) -> int:
#         length = len(nums)
#         if length == 0:
#             return 0
#
#         res = []
#         num = 0
#
#         for i in range(length):
#             temp = nums[i]
#             if not res or res[-1] < temp:
#                 res.append(temp)
#             else:
#                 for j in range(len(res)):
#                     if temp > res[j]:
#                         res.insert(j+1, temp)
#                         break
#         print(res)


class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        length = len(nums)
        if length == 0:
            return 0

        res = sorted(nums)
        num = 0
        for i in range(0, length, 2):
            num += res[i]

        return num

print(Solution().arrayPairSum([1, 2, 6, 5, 4, 3]))
# print(Solution().arrayPairSum([1,4,3,2]))

# print(sorted([1, 2, 6, 5, 4, 3], reverse=True))