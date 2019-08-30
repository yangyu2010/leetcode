#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


from TreeNode import TreeNode
from TreeNode import preOrderTraverse
from TreeNode import inOrderTraverse
from TreeNode import postOrderTraverse


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        dic = {root: None}

        def bfs(node):
            if node:
                if node.left:
                    dic[node.left] = node
                if node.right:
                    dic[node.right] = node
                bfs(node.left)
                bfs(node.right)
        bfs(root)
        l1, l2 = p, q

        while(l1 != l2):
            l1 = dic.get(l1) if l1 else q
            l2 = dic.get(l2) if l2 else p
            # print(l1, l2)
            if l1:
                print('1-', l1.val)
            if l2:
                print('2-', l2.val)
            print('------')
        return l1



node1 = TreeNode(6)
node2 = TreeNode(2)
node3 = TreeNode(8)

node4 = TreeNode(0)
node5 = TreeNode(4)

node6 = TreeNode(7)
node7 = TreeNode(9)

node8 = TreeNode(3)
node9 = TreeNode(5)


node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node5.left = node8
node5.right = node9

# print('----1----')
# preOrderTraverse(node1)
# print('----2----')
# inOrderTraverse(node1)
# print('----3----')
# postOrderTraverse(node1)
# print('---------')

print(Solution().lowestCommonAncestor(node1, node4, node9).val)

