#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 先序遍历 根->左->右
def preOrderTraverse(node: TreeNode):
    if node:
        print(node.val)
        preOrderTraverse(node.left)
        preOrderTraverse(node.right)


# 中序遍历 左->根->右
def inOrderTraverse(node: TreeNode):
    if node:
        inOrderTraverse(node.left)
        print(node.val)
        inOrderTraverse(node.right)


# 后序遍历 左->右->根
def postOrderTraverse(node: TreeNode):
    if node:
        postOrderTraverse(node.left)
        postOrderTraverse(node.right)
        print(node.val)


# 非递归方式遍历 先序 栈后入先出
def preOrderTraverse2(node: TreeNode):
    cur = node
    stack = []

    while cur or stack:
        if cur:
            print(cur.val)
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack[-1].right
            stack.pop()


# 非递归方式遍历 中序 栈后入先出
def inOrderTraverse2(node: TreeNode):
    cur = node
    stack = []

    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            del_node = stack[-1]
            print(del_node.val)
            cur = del_node.right
            stack.pop()


# 非递归方式遍历 后序 栈后入先出
def postOrderTraverse2(node: TreeNode):
    if not node:
        return False

    stack1 = []
    stack2 = []
    stack1.append(node)

    while stack1:
        cur_node = stack1.pop()
        if cur_node.left:
            stack1.append(cur_node.left)
        if cur_node.right:
            stack1.append(cur_node.right)
        stack2.append(cur_node)

    while stack2:
        print(stack2.pop().val)


# 层级遍历 队列先入先出
def levelOrderTraverse(node: TreeNode):
    if not node:
        return False
    queue = []
    queue.append(node)

    while queue:
        temp = queue.pop(0)
        if temp.left:
            queue.append(temp.left)
        if temp.right:
            queue.append(temp.right)
        print(temp.val)


# 最大深度
def maxDepth(node: TreeNode) -> int:
    if not node:
        return 0

    return max(maxDepth(node.left), maxDepth(node.right)) + 1
