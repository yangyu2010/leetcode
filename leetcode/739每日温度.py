#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


# def dailyTemperatures(T: [int]) -> [int]:
#     length = len(T)
#     res = []
#
#     # for j in range(9, 9):
#     #     print(j)
#
#     for i in range(length):
#         current_int = T[i]
#         for j in range(i + 1, length):
#             next_int = T[j]
#             if next_int > current_int:
#                 res.append(j - i)
#                 break
#         else:
#             res.append(0)
#     return res


def dailyTemperatures(T: [int]) -> [int]:
    res_list = [0] * len(T)
    stack_list = []

    for i, temp in enumerate(T):
        while stack_list and T[stack_list[-1]] < temp:
            res_list[stack_list[-1]] = i - stack_list[-1]
            stack_list.pop()
        stack_list.append(i)
    return res_list


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

# print(dailyTemperatures([55, 38, 53, 81, 61, 93, 97, 32, 43, 78]))

