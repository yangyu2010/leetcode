#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


# def spiralOrder(matrix: [[int]]) -> [int]:
#     m = len(matrix)
#     n = len(matrix[0]) if m > 0 else 0
#     bxFlag = True
#     nums = []
#     if n == 0 or m == 0: return nums
#
#     x = 0
#     y = 0
#     print(matrix[x][y])
#     nums.append(matrix[x][y])
#
#     for i in range(min(m, n)):
#         if bxFlag:
#             while y < n - 1:
#                 y += 1
#                 print(matrix[x][y])
#                 nums.append(matrix[x][y])
#             else:
#                 while x < m - 1:
#                     x += 1
#                     print(matrix[x][y])
#                     nums.append(matrix[x][y])
#             n -= 1
#             m -= 1
#         else:
#             while y >= (i-1)/2 and y > 0:
#                 y -= 1
#                 print(matrix[x][y])
#                 nums.append(matrix[x][y])
#             else:
#                 while x >= (i-1)/2 and x > 1:
#                     x -= 1
#                     print(matrix[x][y])
#                     nums.append(matrix[x][y])
#         if m == 0 or n == 0:
#             break
#         bxFlag = not bxFlag
#     return nums


def spiralOrder(matrix: [[int]]) -> [int]:
    m = len(matrix)
    n = len(matrix[0]) if m > 0 else 0
    bxFlag = True
    nums = []
    if n == 0 or m == 0: return nums

    x = 0
    y = 0
    print(matrix[x][y])
    nums.append(matrix[x][y])

    for i in range(3):
        while y < n - 1:
            y += 1
            print(matrix[x][y])
            nums.append(matrix[x][y])
        while x < m - 1:
            x += 1
            print(matrix[x][y])
            nums.append(matrix[x][y])
        m -= 1
        n -= 1

        while y > i:
            y -= 1
            nums.append(matrix[x][y])
            print(matrix[x][y])
        while x > i + 1:
            x -= 1
            nums.append(matrix[x][y])
            print(matrix[x][y])
        print('-----', x, y)

    return nums

# nums = [
#     [ 1, 2, 3 ],
#     [ 4, 5, 6 ],
#     [ 7, 8, 9 ]
# ]

# nums = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]

# nums = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11,12,13,14,15],
#     [16,17,18,19,20],
#     [21,22,23,24,25]
# ]

nums = [
    [2,3,4],
    [5,6,7],
    [8,9,10],
    [11,12,13],
    [14,15,16]
]

# nums = [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12],
#   [13,14,15,16],
# ]

# nums = [[1,2,3,4,5,6,7,8,9,10],
#         [11,12,13,14,15,16,17,18,19,20],
#         [21,22,23,24,25,26,27,28,29,30],
#         [31,32,33,34,35,36,37,38,39,40],
#         [41,42,43,44,45,46,47,48,49,50],
#         [51,52,53,54,55,56,57,58,59,60],
#         [61,62,63,64,65,66,67,68,69,70],
#         [71,72,73,74,75,76,77,78,79,80],
#         [81,82,83,84,85,86,87,88,89,90],
#         [91,92,93,94,95,96,97,98,99,100]]

# nums = [[1], [2], [3]]

print(spiralOrder(nums))
