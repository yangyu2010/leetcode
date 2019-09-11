#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


# def strStr(haystack: str, needle: str) -> int:
#     if needle == '':
#         return 0
#     if len(needle) > len(haystack):
#         return -1
#
#     start_index: int = -1
#     end_index: int = -1
#     check_index = 0
#
#     for i in range(len(haystack)):
#         # print(i)
#         s_check = haystack[i]
#         if check_index >= len(needle):
#             return start_index
#
#         if s_check == needle[check_index]:
#             check_index += 1
#             if start_index == -1:
#                 start_index = i
#         else:
#             if start_index != -1:
#                 end_index = i
#             if end_index - start_index == len(needle):
#                 return start_index
#             else:
#                 check_index = 0
#                 start_index = -1
#                 end_index = -1
#
#     return start_index


def strStr(haystack: str, needle: str) -> int:
    if needle == '':
        return 0
    length_h = len(haystack)
    length_n = len(needle)
    if length_n > length_h:
        return -1

    for i in range(length_h - length_n + 1):
        # print(i)
        sub_str = haystack[i:i+length_n]
        #print(sub_str)
        if sub_str == needle:
            return i
    return -1

print(strStr("mississippi", "issip"))
# print(strStr("mississippi", "issip"))
