#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


from TreeNode import TreeNode


# class Solution:
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         if not root:
#             return False
#
#         res = [(root, sum - root.val)]
#         while res:
#             cur_node, cur_sum = res.pop()
#             if not cur_node.left and not cur_node.right and cur_sum == 0:
#                 return True
#             if cur_node.right:
#                 res.append((cur_node.right, cur_sum - cur_node.right.val))
#             if cur_node.left:
#                 res.append((cur_node.left, cur_sum - cur_node.left.val))
#         return False


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


node1 = TreeNode(5)
node2 = TreeNode(4)
node3 = TreeNode(8)
node4 = TreeNode(11)
node5 = TreeNode(13)
node6 = TreeNode(4)
node7 = TreeNode(7)
node8 = TreeNode(2)
node9 = TreeNode(1)


node1.left = node2
node2.left = node4
node4.left = node7
node4.right = node8

node1.right = node3
node3.left = node5
node3.right = node6
node6.right = node9

print(Solution().hasPathSum(node1, 26))