# -*- coding: utf-8 -*-

'''
@Author: YangYu
@Github: https://github.com/yangyu2010
@Date: 2019-07-11 17:28:23
@LastEditors: YangYu
@LastEditTime: 2019-09-03 16:29:19
'''

class Solution:
    def isValid(self, s: str) -> bool:
        map_d = {")": "(", "}": "{", "]": "["}
        length = len(s)
        # 长度是基数直接返回
        if length % 2 != 0:
            return False
        stack = []
        for temp in s:
            if temp in map_d:
                top_element = stack.pop() if stack else '#'
                if map_d[temp] != top_element:
                    return False
            else:
                stack.append(temp)
        return not stack

    def isValid2(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return len(s) == 0
        

obj = Solution()
print(obj.isValid2('{[]}'))
# print(obj.isValid2('[]{'))