#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class Solution:
    def search(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
            elif nums[mid] > target:
                right -= 1
        return -1


# print(Solution().search([-1,0,3,5,9,12], 9))
print(Solution().search([-1,0,3,5,9,12], 2))
