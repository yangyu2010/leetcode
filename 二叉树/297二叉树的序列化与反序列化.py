#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


from TreeNode import TreeNode
from TreeNode import preOrderTraverse
from TreeNode import inOrderTraverse
from TreeNode import postOrderTraverse


class Codec:

    def serialize(self, root: TreeNode):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def rserialize(node: TreeNode, string: str):
            if node is None:
                string += 'None,'
            else:
                string += str(node.val) + ','
                string = rserialize(node.left, string)
                string = rserialize(node.right, string)
            return string
        return rserialize(root, '')

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def rdeserialize(l: [str]):
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
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
#
# node5.left = node8
# node5.right = node9

node_str = Codec().serialize(node1)
print(node_str)
tree = Codec().deserialize(node_str)
print('----1----')
preOrderTraverse(tree)
print('----2----')
inOrderTraverse(tree)
print('----3----')
postOrderTraverse(tree)

