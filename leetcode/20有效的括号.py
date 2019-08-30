#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class Solution:

    def isValid(self, s: str) -> bool:

        map_d = {")": "(", "}": "{", "]": "["}

        length = len(s)
        # 长度是基数直接返回
        if length % 2 != 0:
            return False

        stack = []
        for temp in s:
            if temp in map_d:
                top_element = stack.pop() if stack else '#'
                if map_d[temp] != top_element:
                    return False
            else:
                stack.append(temp)
        return not stack






obj = Solution()
print(obj.isValid('{[]}'))

