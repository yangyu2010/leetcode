#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


def evalRPN(tokens: [str]) -> int:
    stack = []
    for s in tokens:
        if s.lstrip('-').isdigit():
            stack.append(int(s))
        else:
            temp2 = stack.pop()
            temp1 = stack.pop()
            if s == '+':
                stack.append(temp1 + temp2)
            elif s == '-':
                stack.append(temp1 - temp2)
            elif s == '/':
                stack.append(int(temp1 / temp2))
            elif s == '*':
                stack.append(temp1 * temp2)
            else:
                print('当前字符串匹配失败', s)
                return 0
    return stack[0] if stack else 0


# print(evalRPN(["2", "1", "+", "3", "*"]))
print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))