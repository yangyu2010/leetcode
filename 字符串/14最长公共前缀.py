#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang

'''
    水平扫描法
'''
def longestCommonPrefix(strs: [str]) -> str:
    if len(strs) == 0:
        return ''
    res = strs[0]

    for i in range(len(strs)):
        # while not res in strs[i]:
        while strs[i].find(res) != 0:
            res = res[:-1]
            if not res:
                return ''
    return res


# print(longestCommonPrefix(["flower", "flow", "floight"]))
# print(longestCommonPrefix(["c", "acc", "ccc"]))
print(longestCommonPrefix(["abcd", "abc", "ab"]))