#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


from TreeNode import TreeNode
from TreeNode import preOrderTraverse
from TreeNode import inOrderTraverse
from TreeNode import postOrderTraverse


class Solution:

    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if len(inorder) == 0:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root


# tree = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
tree = Solution().buildTree([11, 7, 5, 3, 6, 9, 8, 10, 15, 13, 12, 14, 20, 18, 25], [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 20, 25])

print('----1----')
preOrderTraverse(tree)
print('----2----')
inOrderTraverse(tree)
print('----3----')
postOrderTraverse(tree)
