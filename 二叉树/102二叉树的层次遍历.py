#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


from TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return None

        ans = []
        level = [root]

        while level:
            cur = []
            next_level = []

            for node in level:
                cur.append(node.val)

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            ans.append(cur)
            level = next_level

        return ans


# class Solution:
#     def levelOrder(self, root: TreeNode) -> [[int]]:
#         if not root:
#             return None
#
#         res = []
#         queue = []
#         queue.append(root)
#
#         while queue:
#             size = len(queue)
#             level = []
#
#             for i in range(size):
#                 pre_node = queue.pop(0)
#                 level.append(pre_node.val)
#
#                 if pre_node.left:
#                     queue.append(pre_node.left)
#                 if pre_node.right:
#                     queue.append(pre_node.right)
#
#             res.append(level)
#
#         return res


node1 = TreeNode(10)
node2 = TreeNode(9)
node3 = TreeNode(20)
node4 = TreeNode(15)
node5 = TreeNode(35)
node6 = TreeNode(7)
node7 = TreeNode(8)


node1.left = node2
node1.right = node3
node3.left = node4
node3.right = node5

node2.left = node6
# node2.right = node7

print(Solution().levelOrder(node1))
