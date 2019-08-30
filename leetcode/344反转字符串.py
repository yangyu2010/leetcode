#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang

class Solution:
    def reverseString(self, s: [str]) -> [str]:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        if length == 0:
            return None

        start_index = 0
        end_index = length - start_index - 1

        for i in range(length // 2):
            if start_index == end_index:
                return
            else:
                temp = s[start_index]
                s[start_index] = s[end_index]
                s[end_index] = temp
                start_index += 1
                end_index = length - start_index - 1
        return s


# Solution().reverseString(["h", "e", "l", "l", "o"])
Solution().reverseString(["H","a","n","n","a","h"])
