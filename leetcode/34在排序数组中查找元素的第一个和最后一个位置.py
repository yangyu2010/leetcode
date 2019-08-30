#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class Solution:
    def left_bound(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            guess = nums[mid]
            if guess == target:
                right = mid
            elif guess < target:
                left = mid + 1
            elif guess > target:
                right = mid
        return left

    def right_bound(self, nums: [int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            guess = nums[mid]
            if guess == target:
                left = mid + 1
            elif guess < target:
                left = mid + 1
            elif guess > target:
                right = mid
        return left - 1


print(Solution().left_bound([1, 2, 2, 2, 3], 3))
print(Solution().right_bound([1, 2, 2, 2, 3], 3))
