#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


# def lengthOfLongestSubstring(s: str) -> int:
#     if s == '':
#         return 0
#     max_num = 0
#     for i in range(len(s)):
#         temp_arr = []
#         temp_arr.append(s[i])
#         for j in range(i+1, len(s)):
#             s_current = s[j]
#             if s_current not in temp_arr:
#                 temp_arr.append(s_current)
#             else:
#                 if j - i > max_num:
#                     max_num = j - i
#                 break
#         if len(temp_arr) > max_num:
#             max_num = len(temp_arr)
#     return max_num


def lengthOfLongestSubstring(s: str) -> int:
    if s == '':
        return 0
    start = 0
    end = 0
    ans = 0
    map_s = {}

    for i in range(len(s)):
        end = i
        temp_s = s[i]
        if temp_s in map_s:
            index = map_s[temp_s]
            start = max(index, start)
        map_s[temp_s] = end + 1
        ans = max(end-start+1, ans)
    return ans


print(lengthOfLongestSubstring("accsdbbbbb"))

