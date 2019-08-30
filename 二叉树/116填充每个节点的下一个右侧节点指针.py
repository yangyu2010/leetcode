#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def connect(self, root: TreeNode) -> TreeNode:
        if not root: return None
        queue = [root]
        while queue:
            node_pre = None
            for i in range(len(queue)):
                node_cur = queue.pop(0)
                if node_pre:
                    node_pre.next = node_cur
                node_pre = node_cur
                if node_cur.left or node_cur.right:
                    queue.append(node_cur.left)
                    queue.append(node_cur.right)
        return root

    def connect2(self, root: TreeNode) -> TreeNode:
        if not root: return None
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect2(root.left)
        self.connect2(root.right)
        return root




node1 = TreeNode(6)
node2 = TreeNode(2)
node3 = TreeNode(8)

node4 = TreeNode(0)
node5 = TreeNode(4)

node6 = TreeNode(7)
node7 = TreeNode(9)

# node8 = TreeNode(3)
# node9 = TreeNode(5)


node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

# node5.left = node8
# node5.right = node9


def preOrderTraverse(node: TreeNode):
    if node:
        print(node.val)
        if node.next:
            print(node.next.val)
        print('-------')
        preOrderTraverse(node.left)
        preOrderTraverse(node.right)


node = Solution().connect2(node1)

preOrderTraverse(node)
