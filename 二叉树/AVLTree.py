#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0


# 先序遍历 根->左->右
def preOrderTraverse(node: TreeNode):
    if node:
        print(node.val)
        preOrderTraverse(node.left)
        preOrderTraverse(node.right)


# 中序遍历 左->根->右
def inOrderTraverse(node: TreeNode):
    if node:
        inOrderTraverse(node.left)
        print(node.val)
        inOrderTraverse(node.right)


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node: TreeNode):
        if node is None:
            return -1
        else:
            return node.height

    def update_height(self, node: TreeNode):
        if node is None:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def unbalance(self, node) -> bool:
        return abs(self.height(node.left) - self.height(node.right)) > 1

    def find(self, val):
        if self.root is None:
            return None
        else:
            return self._find(val, self.root)

    def _find(self, val, node):
        if node is None:
            return None
        elif val < node.val:
            return self._find(val, node.left)
        elif val > node.val:
            return self._find(val, node.right)
        else:
            return node

    def findMin(self):
        if self.root is None:
            return None
        else:
            return self._findMin(self.root)

    def _findMin(self, node):
        if node.left:
            return self._findMin(node.left)
        else:
            return node

    def findMax(self):
        if self.root is None:
            return None
        else:
            return self._findMax(self.root)

    def _findMax(self, node):
        if node.right:
            return self._findMax(node.right)
        else:
            return node

    '''
    右旋转, 处理LL的情况
    '''
    def left_rotate(self, node: TreeNode):
        left = node
        root = node.right
        left.right = root.left
        root.left = left

        self.update_height(left)
        self.update_height(root)

        return root

    '''
    左旋转, 处理RR的情况
    '''
    def right_rotate(self, node: TreeNode):
        right = node
        root = node.left
        right.left = root.right
        root.right = right

        self.update_height(right)
        self.update_height(root)

        return root

    '''
    双向旋转（先右后左）平衡处理RL
    '''
    def right_left_rotate(self, node: TreeNode):
        node.right = self.right_rotate(node.right)
        return self.left_rotate(node)

    '''
    双向旋转（先左后右）平衡处理LR
    '''
    def left_right_rotate(self, node: TreeNode):
        node.left = self.left_rotate(node.left)
        return self.right_rotate(node)

    def insert(self, val: int):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.root = self.__insert__(val, self.root)

    def __insert__(self, val: int, node: TreeNode):
        if node is None:
            node = TreeNode(val)
        elif val < node.val:
            node.left = self.__insert__(val, node.left)
            if self.unbalance(node):
                # LL不平衡
                if val < node.left.val:
                    node = self.right_rotate(node)
                else:
                    # LR不平衡
                    node = self.left_right_rotate(node)
        elif val > node.val:
            node.right = self.__insert__(val, node.right)
            if self.unbalance(node):
                # RL不平衡
                if val < node.right.val:
                    node = self.right_left_rotate(node)
                else:
                    # RR不平衡
                    node = self.left_rotate(node)

        self.update_height(node)
        return node

    def delete(self, val):
        node = self.find(val)
        if node:
            self.root = self._remove(val, self.root)

    def _remove(self, val: int, node: TreeNode):
        if node is None:
            node = TreeNode(val)
        elif val < node.val:
            node.left = self._remove(val, node.left)
            if self.unbalance(node):
                if self.height(node.right.right) >= self.height(node.right.left):
                    node = self.right_rotate(node)
                else:
                    node = self.right_left_rotate(node)
        elif val > node.val:
            node.right = self._remove(val, node.right)
            if self.unbalance(node):
                if self.height(node.left.left) >= self.height(node.left.right):
                    node = self.left_rotate(node)
                else:
                    node = self.left_right_rotate(node)

        elif node.right and node.left:
            if node.left.height <= node.right.height:
                min_node = self._findMin(node.right)
                node.val = min_node.val
                node.right = self._remove(node.val, node.right)
            else:
                max_node = self._findMax(node.left)
                node.key = max_node.key
                node.left = self._remove(node.key, node.left)
        else:
            if node.right:
                node = node.right
            elif node.left:
                node = node.left
            else:
                node = None

        self.update_height(node)
        return node


"""测试"""
Array = map(int, "6 4 7 3 5 1 2".split())
tree = AVLTree()
for i in Array:
    # print(i)
    tree.insert(i)
    # print(Tree.root.val)

print('----1-----')
preOrderTraverse(tree.root)
print('----2-----')
inOrderTraverse(tree.root)
print('----3-----')

node1 = tree.find(1)
if node1:
    print(node1.val)

# tree.delete(3)
# tree.delete(2)
# tree.delete(1)
tree.delete(10)

print('----1-----')
preOrderTraverse(tree.root)
print('----2-----')
inOrderTraverse(tree.root)
print('----3-----')
