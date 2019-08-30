#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


def findDiagonalOrder(matrix: [[int]]) -> [int]:
    m = len(matrix)
    n = len(matrix[0]) if m > 0 else 0
    nums = []
    bxFlag = True
    if n == 0 or m == 0: return nums

    for i in range(m + n - 1):
        pm = m if bxFlag else n
        pn = n if bxFlag else m
        x = i if i < pm else pm - 1
        y = i - x

        while (x >= 0 and y < pn):
            if bxFlag:
                nums.append(matrix[x][y])
            else:
                nums.append(matrix[y][x])
            x -= 1
            y += 1

        bxFlag = not bxFlag

    return nums


# nums = [
#     [1, 2, 3, 4],
#     [4, 5, 6, 4],
#     [7, 8, 9, 4]
# ]

# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

nums = [[2,3]]

# nums = [[3], [2], [4], [5]]
# nums = [[2,5],[8,4],[0,1]]

print(findDiagonalOrder(nums))
