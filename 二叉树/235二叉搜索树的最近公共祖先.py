#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


from TreeNode import TreeNode
from TreeNode import preOrderTraverse
from TreeNode import inOrderTraverse
from TreeNode import postOrderTraverse


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None

        if not p or not q:
            return None

        if q.val > root.val and p.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif q.val < root.val and p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


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

print('----1----')
preOrderTraverse(node1)
print('----2----')
inOrderTraverse(node1)
print('----3----')
postOrderTraverse(node1)

print(Solution().lowestCommonAncestor(node1, node4, node9).val)
