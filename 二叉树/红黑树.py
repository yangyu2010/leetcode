#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class RBNode:
    def __init__(self, val, color='R'):
        self.val = val
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def is_black_node(self):
        return self.color == 'B'

    def is_red_node(self):
        return self.color == 'R'

    def set_red_node(self):
        self.color = 'R'

    def set_black_node(self):
        self.color = 'B'

    def print(self):
        if self.left:
            self.left.print()
        print(self.val)
        if self.right:
            self.right.print()


class RBTree:
    def __init__(self):
        self.root = None

    def print(self):

        # 先序遍历 根->左->右
        def preOrderTraverse(node: RBNode):
            if node:
                print(node.val, node.color)
                preOrderTraverse(node.left)
                preOrderTraverse(node.right)

        # 中序遍历 左->根->右
        def inOrderTraverse(node: RBNode):
            if node:
                inOrderTraverse(node.left)
                print(node.val, node.color)
                inOrderTraverse(node.right)

        # 后序遍历 左->右->根
        def postOrderTraverse(node: RBNode):
            if node:
                postOrderTraverse(node.left)
                postOrderTraverse(node.right)
                print(node.val, node.color)

        print('----1----')
        preOrderTraverse(self.root)
        print('----2----')
        inOrderTraverse(self.root)
        print('----3----')
        postOrderTraverse(self.root)
        print('----over----')

    def left_rotate(self, node: RBNode):
        parent = node.parent
        right = node.right

        node.right = right.left
        if node.right:
            node.right.parent = node

        right.left = node
        node.parent = right

        right.parent = parent
        if not parent:
            self.root = right
        else:
            if parent.left == node:
                parent.left = right
            else:
                parent.right = right

    def right_rotate(self, node: RBNode):
        parent = node.parent
        left = node.left

        left.right = node
        node.parent = left

        left.parent = parent
        if not parent:
            self.root = left
        else:
            if parent.left == node:
                parent.left = left
            else:
                parent.right = left

    def add_node(self, node):
        # self.action = 'inser node {}'.format(node.val)
        self.insert_node(node)
        self.check_node(node)
        pass

    def insert_node(self, node: RBNode):
        if not self.root:
            self.root = node
            return

        cur = self.root
        while cur:
            if cur.val < node.val:
                if not cur.right:
                    node.parent = cur
                    cur.right = node
                    break
                cur = cur.right
            elif cur.val > node.val:
                if not cur.left:
                    node.parent = cur
                    cur.left = node
                    break
                cur = cur.left

    def check_node(self, node: RBNode):
        # 如果当前节点或者当前节点的父节点是root, 直接设置root为黑色, 退出
        if self.root == node or self.root == node.parent:
            self.root.set_black_node()
            return

        # 如果父节点是黑色节点, 直接退出
        if node.parent.is_black_node():
            return

        # 父节点和叔节点都是红色 进行变色
        '''
        当前节点(即，被插入节点)是红色，其父节点也为红色，违背了"性质4 不能连续的两个红色节点"
        解决方案:
            1.将“父节点”设为黑色。
            2.将“叔叔节点”设为黑色。
            3.将“祖父节点”设为“红色”。
            4.将“祖父节点”设为“当前节点”(红色节点)；继续对“当前节点”进行修复操作。
        '''
        grand = node.parent.parent
        if not grand:
            self.check_node(node.parent)
            return
        if grand.left and grand.left.is_red_node() and grand.right and grand.right.is_red_node():
            grand.left.set_black_node()
            grand.right.set_black_node()
            grand.set_red_node()
            self.check_node(grand)
            return

        # node node.parent node.parent.parent 不同边
        '''
        叔叔是黑色（或缺失），且祖父节点、父节点和新节点不处于一条斜线上。
        解决方案:
            1.将“父节点”作为“新的当前节点”。
            2.以“新的当前节点”为支点进行旋转（左或者右）。
            3.检测新的节点
        '''
        parent = node.parent
        if parent.left == node and grand.right == node.parent:
            self.right_rotate(node.parent)
            self.check_node(parent)
            return
        if parent.right == node and grand.left == node.parent:
            parent = node.parent
            self.left_rotate(node.parent)
            self.check_node(parent)
            return

        # node node.parent node.parent.parent 同边
        '''
        叔叔是黑色（或缺失），且祖父节点、父节点和新节点处于一条斜线上
        解决方案:
            1.将“父节点”设为“黑色”。
            2.将“祖父节点”设为“红色”。
            3.以“祖父节点”为支点进行旋转（左或者右）。
        '''
        parent.set_black_node()
        grand.set_red_node()
        if parent.left == node and grand.left == node.parent:
            self.right_rotate(grand)
            return
        if parent.right == node and grand.right == node.parent:
            self.left_rotate(grand)
            return




tree = RBTree()
node1 = RBNode(5)
node2 = RBNode(14)
node3 = RBNode(16)

tree.add_node(node1)
tree.add_node(node2)
tree.print()
tree.add_node(node3)
tree.print()


