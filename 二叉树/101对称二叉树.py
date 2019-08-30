#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


'''
    1
   / \
  2   2
 / \ / \
3  4 4  3
'''


from TreeNode import TreeNode


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        res = []
        res.append(root)
        res.append(root)

        while res:
            node1 = res.pop()
            node2 = res.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            res.append(node1.left)
            res.append(node2.right)
            res.append(node1.right)
            res.append(node2.left)

        return True


# class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     if root is None:
    #         return False
    #     return self.isMirror(root, root)
    #
    # def isMirror(self, node1: TreeNode, node2: TreeNode) -> bool:
    #     if not node1 and not node2:
    #         return True
    #     if not node1 or not node2:
    #         return False
    #     return node1.val == node2.val and \
    #            self.isMirror(node1.left, node2.right) and \
    #            self.isMirror(node1.right, node2.left)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(2)
node4 = TreeNode(3)
node5 = TreeNode(4)
node6 = TreeNode(4)
node7 = TreeNode(3)

node1.left = node2
node1.right = node3

# node2.left = node4
node2.right = node5

# node3.left = node6
node3.right = node7

print(Solution().isSymmetric(node1))
