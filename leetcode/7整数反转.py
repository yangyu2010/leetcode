#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang

import sys

# print(sys.maxsize)
# print(pow(2, 31))

#
# def reverse(x: int) -> int:
#     if x > pow(2, 31) - 1 or x < -pow(2, 31):
#         return 0
#
#     negative = x < 0
#     if negative:
#         x = -x
#     arr = []
#     while x != 0:
#         # print(x % 10)
#         # print(x // 10)
#         # x = x // 10
#         arr.insert(0, x % 10)
#         x = x // 10
#
#     ans = 0
#     # for i in range(len(arr)):
#     #     if negative:
#     #         ans -= arr[i] * pow(10, i)
#     #     else:
#     #         ans += arr[i] * pow(10, i)
#     #
#     if ans > pow(2, 31) - 1 or ans < -pow(2, 31):
#         return 0
#     else:
#         return ans


def reverse(x: int) -> int:
    res = 0
    max_num = pow(2, 31) - 1
    min_num = pow(-2, 31)

    negative = 0
    if x < 0:
        x = -x
        negative = 1

    while x != 0:
        pop = x % 10
        if res > max_num / 10 or (res == max_num / 10 and pop > 7):
            return 0
        if res < min_num / 10 or (res == min_num / 10 and pop < -8):
            return 0
        res = res * 10 + pop
        x = x // 10
    if negative:
        return -res
    else:
        return res


print(reverse(123))
#               2147483647 321

# print(-pow(2, 31))
# print(pow(2, 31) - 1)