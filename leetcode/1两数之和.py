#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


# https://leetcode-cn.com/problems/two-sum/

def twoSum(nums:[int], target: int):
    hashmap = {}
    for i in range(len(nums)):
        print(i)
        num = nums[i]
        if target - num in hashmap:
            print(hashmap[target - num], i)
            break
        else:
            hashmap[num] = i



# twoSum([1,2,4,2,3,4,5], 3)



class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        hashmap = {}
        print(enumerate(nums))
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            else:
                hashmap[num] = index
        else:
            return None




list = Solution().twoSum([2,7,11,15], 18)
print(list)
