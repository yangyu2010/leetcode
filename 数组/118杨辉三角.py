#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class Solution:
    def generate(self, numRows: int) -> [[int]]:
        res = []

        for i in range(numRows):
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1

            for j in range(1, len(row) - 1):
                row[j] = res[-1][j-1] + res[-1][j]

            res.append(row)

        print(res)
        return res


Solution().generate(5)

