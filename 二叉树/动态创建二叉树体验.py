#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang

from 二叉树 import TreeNode
from 二叉树 import preOrderTraverse
from 二叉树 import inOrderTraverse
from 二叉树 import postOrderTraverse


def creatTree(list: [int]):

    rootTree = None
    for i in list:
        cur_tree = TreeNode(i)
        if not rootTree:
            rootTree = cur_tree
            continue
        else:
            temp = rootTree
            while temp:
                if temp.val < cur_tree.val:
                    if not temp.rightNode:
                        temp.rightNode = cur_tree
                        temp = None
                    else:
                        temp = temp.rightNode
                else:
                    if not temp.leftNode:
                        temp.leftNode = cur_tree
                        temp = None
                    else:
                        temp = temp.leftNode

    preOrderTraverse(rootTree)
    print('----1----')
    inOrderTraverse(rootTree)
    print('----2----')
    postOrderTraverse(rootTree)


creatTree([10,9,20,15,35,7,8])

'''
10
9
7
8
20
15
35
----1----
9
7
8
10
20
15
35
----2----
9
7
8
20
15
35
10
'''