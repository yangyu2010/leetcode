#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu


# def myAtoi(str: str) -> int:
#     negative = 1
#     res = ""
#     for s in str:
#         if str.index(s) == 0:
#             if s == '-':
#                 negative = 0
#             else:
#                 if s.isdigit():
#                     res += s
#                 else:
#                     return 0
#         else:
#             if s.isdigit():
#                 res += s
#             else:
#                 return int(res) if negative else -int(res)
#     return int(res) if negative else -int(res)


# def myAtoi(str: str) -> int:
#     not_netgative = 1
#     res = 0
#     max_num = pow(2, 31) - 1
#     min_num = pow(-2, 31)
#
#     for s in str:
#         # 第一位
#         if str.index(s) == 0:
#             if s == '-':
#                 not_netgative = 0
#             else:
#                 if s.isdigit():
#                     res = res * 10 + int(s)
#                 else:
#                     break
#         else:
#             # 从第2位开始
#             if s.isdigit():
#                 pop = int(s)
#                 if res > max_num // 10 or (res == max_num // 10 and pop > 7):
#                     return max_num
#                 if res < -(min_num // -10) or (res == -(min_num // -10) and pop > 8):
#                     return min_num
#                 if not_netgative:
#                     res = res * 10 + pop
#                 else:
#                     res = res * 10 - pop
#             else:
#                 break
#     return res


# def myAtoi(str: str) -> int:
#     netgative = False
#     res = 0
#     max_num = pow(2, 31) - 1
#     min_num = pow(-2, 31)
#     start = False
#     for s in str:
#         if start == False:
#             if s == ' ':
#                 continue
#             else:
#                 if s == '-':
#                     start = True
#                     netgative = True
#                 elif s == '+':
#                     start = True
#                     continue
#                 elif s.isdigit():
#                     start = True
#                     res = res * 10 + int(s)
#                 else:
#                     break
#         else:
#             if s.isdigit():
#                 pop = int(s)
#                 if res > max_num // 10 or (res == max_num // 10 and pop > 7):
#                     return max_num
#                 if res < -(min_num // -10) or (res == -(min_num // -10) and pop > 8):
#                     return min_num
#                 if netgative:
#                     res = res * 10 - pop
#                 else:
#                     res = res * 10 + pop
#             else:
#                 break
#     return res


import re


def myAtoi(str: str) -> int:
    re_result = re.search(r'^[\+\-]?\d+', str.lstrip())
    res = 0
    if re_result:
        res = int(re_result.group())
        # res = min(max(2**31 - 1, res), -2**31)
        res = min(max(res, -2**31), 2**31 - 1)
    return res


# print(myAtoi(' -42'))
# print(myAtoi('91283472332w'))
# print(myAtoi('   w42'))
print(myAtoi("words and 987"))


