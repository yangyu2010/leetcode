#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


# def rotate(nums: [int], k: int) -> None:
#     for i in range(k):
#         nums.insert(0, nums.pop())
#     print(nums)


# 不行
# def rotate(nums: [int], k: int) -> None:
#     for i in range(k % len(nums)):
#         start_index = i
#         end_index = len(nums) - k + i
#         temp = nums[start_index]
#         nums[start_index] = nums[end_index]
#         nums[end_index] = temp
#     print(nums)


# def rotate(nums: [int], k: int) -> None:
#     for i in range(k):
#         previous = nums[len(nums) - 1]
#         for j in range(len(nums)):
#             temp = nums[j]
#             nums[j] = previous
#             previous = temp
#     print(nums)

# def rotate(nums: [int], k: int) -> None:
#     a = [None] * len(nums)
#
#     for i in range(len(nums)):
#         print((i + k) % len(nums))
#         a[(i + k) % len(nums)] = nums[i]
#
#     print(a)


def rotate(nums: [int], k: int) -> None:
    k %= len(nums)
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)
    print(nums)

def reverse(nums: [int], start: int, end: int):
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1

rotate([1,2,3,4,5,6,7], 3)