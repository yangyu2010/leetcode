#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        prev = []

        for i in range(rowIndex+1):
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = prev[j-1] + prev[j]

            prev = row

        print(prev)
        return prev

Solution().getRow(3)