#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


from TreeNode import TreeNode
from TreeNode import preOrderTraverse
from TreeNode import inOrderTraverse
from TreeNode import postOrderTraverse


class Solution:
    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        return root


# inorder[mid+1:]   [12, 13, 14, 15, 18, 20, 25]
# postorder[mid:-1] [12, 14, 13, 18, 25, 20, 15]

# inorder[:mid]     [3, 5, 6, 7, 8, 9, 10]
# postorder[:mid]   [3, 6, 5, 8, 10, 9, 7]



tree = Solution().buildTree([3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 20, 25], [3, 6, 5, 8, 10, 9, 7, 12, 14, 13, 18, 25, 20, 15, 11])

print('----1----')
preOrderTraverse(tree)
print('----2----')
inOrderTraverse(tree)
print('----3----')
postOrderTraverse(tree)
