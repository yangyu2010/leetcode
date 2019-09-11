#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.strip().split()
        start = 0
        end = len(l)-1
        while start < end:
            temp = l[start]
            l[start] = l[end]
            l[end] = temp
            start += 1
            end -= 1
        return ' '.join(l)

    # def reverseWords(self, s: str) -> str:
    #     return " ".join(s.split()[::-1])

    # def reverseWords(self, s: str) -> str:
    #     self.swap(s, 0, len(s)-1)
    #     print(s)
    #
    # def swap(self, s: str, start: int, end: int):
    #     while start < end:
    #         temp = s[start]
    #         s[start] = s[end]
    #         s[end] = temp
    #         start += 1
    #         end -= 1


# print(Solution().reverseWords('the sky is blue'))

# print(Solution().reverseWords("  hello world!  "))

print(Solution().reverseWords("a good   example"))
