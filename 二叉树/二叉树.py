#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


from TreeNode import TreeNode


# 二叉搜索树
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 插入val
    def insert(self, val: int):
        node = TreeNode(val)
        if not self.root:
            self.root = node
        else:
            self.__insertNode(node)

    # 插入node 内部使用
    def __insertNode(self, node: TreeNode):
        temp = self.root
        while temp:
            if temp.val > node.val:
                if not temp.left:
                    temp.left = node
                    temp = None
                else:
                    temp = temp.left
            else:
                if not temp.right:
                    temp.right = node
                    temp = None
                else:
                    temp = temp.right

    # 最大值
    def max(self) -> int:
        temp = self.root
        while temp:
            if temp.right:
                temp = temp.right
            else:
                return temp.val
        else:
            return -1

    # 最小值
    def min(self) -> int:
        temp = self.root
        while temp:
            if temp.left:
                temp = temp.left
            else:
                return temp.val
        else:
            return -1

    # 查找
    def search(self, val: int) -> bool:
        temp = self.root
        while temp:
            if temp.val > val:
                temp = temp.left
            elif temp.val < val:
                temp = temp.right
            else:
                return True
        else:
            return False

    # 移除
    def remove(self, val: int) -> bool:
        pre = self.root
        cur = self.root
        is_left = False

        while cur.val != val:
            pre = cur
            if cur.val > val:
                is_left = True
                cur = cur.left
            else:
                is_left = False
                cur = cur.right
            # 没找到
            if not cur:
                return False

        # 开始删除操作
        if not cur.left and not cur.right:
            # 叶子节点
            if cur == self.root:
                self.root = None
            elif is_left:
                pre.left = None
            else:
                pre.right = None
        elif not cur.left:
            # 没有左节点 只有右节点
            if cur == self.root:
                self.root = cur.right
            elif is_left:
                pre.left = cur.right
            else:
                pre.right = cur.right
        elif not cur.right:
            # 没有右节点 只有左节点
            if cur == self.root:
                self.root = cur.left
            elif is_left:
                pre.left = cur.left
            else:
                pre.right = cur.left
        else:
            successor = self.getSuccessor(cur)

            if cur == self.root:
                self.root = successor
            elif is_left:
                pre.left = successor
            else:
                pre.right = successor

            # 设置左边的
            successor.left = cur.left

            print(successor.val)

        # print(cur.val)
        # print(pre.val)
        # print(is_left)
        return True

    # 找到某个节点的后继节点
    def getSuccessor(self, node: TreeNode) -> TreeNode:
        # 后继节点的父节点
        successor_prev = node
        # 后继节点
        successor = node
        # 当前的节点
        cur_node = node.right

        # 遍历找到节点
        while cur_node:
            successor_prev = successor
            successor = cur_node
            cur_node = cur_node.left

        # 把后继节点的父子关系清空 或 赋值
        if successor != node.right:
            # 一定不能置空 因为successor.right可能有值
            # successor_prev.left = None
            successor_prev.left = successor.right
            successor.right = node.right
        else:
            # 一定不能置空 因为successor.right可能有值
            # node.right = None
            pass

        return successor






# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(9)
# bst.insert(20)
# bst.insert(15)
# bst.insert(35)
# bst.insert(7)
# bst.insert(8)

# print('max value', bst.max())
# print('min value', bst.min())
# print('search', bst.search(8))
# print('remove', bst.remove(9))

# bst.insert(11)
# bst.insert(7)
# bst.insert(15)
# bst.insert(5)
# bst.insert(3)
# bst.insert(9)
# bst.insert(8)
# bst.insert(10)
# bst.insert(13)
# bst.insert(12)
# bst.insert(14)
# bst.insert(20)
# bst.insert(18)
# bst.insert(25)
# bst.insert(6)
# bst.insert(19)

# print('remove', bst.remove(15))

# 先序 11 7 5 3 6 9 8 10 15 13 12 14 20 18 25
# 中序 3 5 6 7 8 9 10 11 12 13 14 15 18 20 25
# 后序 3 6 5 8 10 9 7 12 14 13 18 25 20 15 11

# preOrderTraverse2(bst.root)
# inOrderTraverse2(bst.root)
# postOrderTraverse2(bst.root)

# levelOrderTraverse(bst.root)
# print(maxDepth(bst.root))

# print('----1----')
# preOrderTraverse(bst.root)
# print('----2----')
# inOrderTraverse(bst.root)
# print('----3----')
# postOrderTraverse(bst.root)



# node1 = TreeNode(10)
# node2 = TreeNode(9)
# node3 = TreeNode(20)
# node4 = TreeNode(15)
# node5 = TreeNode(35)
# node6 = TreeNode(7)
# node7 = TreeNode(8)
#
#
# node1.left = node2
# node1.right = node3
# node3.left = node4
# node3.right = node5
#
# node2.left = node6
# node2.right = node7
#
#
# preOrderTraverse(node1)
# print('----1----')
# inOrderTraverse(node1)
# print('----2----')
# postOrderTraverse(node1)

