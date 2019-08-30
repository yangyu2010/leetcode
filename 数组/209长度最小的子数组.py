#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang

'''

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
示例:
输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

'''

import sys

def minSubArrayLen(s: int, nums: [int]) -> int:
    if not len(nums):
        return 0

    begin = 0
    end = 0
    sum = 0
    ans = sys.maxsize

    while end < len(nums):
        if sum + nums[end] < s:
            sum += nums[end]
            end += 1
        else:
            if end - begin < ans:
                ans = end - begin + 1
            sum -= nums[begin]
            begin += 1
    return ans if ans != sys.maxsize else 0


# print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen(3, [1, 1]))