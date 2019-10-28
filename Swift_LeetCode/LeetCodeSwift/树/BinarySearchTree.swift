//
//  BinarySearchTree.swift
//  LeetCodeSwift
//
//  Created by Yang Yu on 2019/9/24.
//  Copyright © 2019 YangYu. All rights reserved.
//  二叉搜索树

class BinarySearchTree<T: Comparable>: BinaryTree<T> {
    
    public func clear() {
        size = 0
    }
    
    func afterAdd(node: Node<T>?) {
        
    }
    
    func afterRemove(node: Node<T>?, replacement: Node<T>?) {
        
    }
    
    func creatNode(element: T, parent: Node<T>?) -> Node<T> {
        return Node(element: element, parent: parent)
    }
    
    public func add(element: T) {
        if root == nil {
            root = creatNode(element: element, parent: nil)
            size += 1;
            afterAdd(node: root)
            return
        }
        
        // 记录当前节点的paretn和方向
        var parent: Node? = root
        var cmp = 0
        
        var node: Node? = root
        while node != nil {
            parent = node
            if node!.element < element {
                node = node?.right
                cmp = 1
            } else if node!.element > element {
                node = node?.left
                cmp = -1
            } else {
                return
            }
        }
        
        let newNode = creatNode(element: element, parent: parent)
        if cmp > 0 {
            parent?.right = newNode
        } else {
            parent?.left = newNode
        }
        size += 1
        
        afterAdd(node: newNode)
    }
    
    public func remove(element: T) {
        guard var node = node(element: element) else { return }
        size -= 1;
        
        // 有两个子节点时 肯定会有前驱节点 找到前驱节点
        if node.hasTwoChildren {
//            let predecessor = node.predecessor!
            let predecessor = node.successor!
            node.element = predecessor.element
            node = predecessor
        }

        // 删除node
        if node.isLeaf { // 叶子节点
            if node.isLeftChild {
                node.parent?.left = nil
            } else if node.isRightChild {
                node.parent?.right = nil
            } else {
                // 没有parent
                root = nil
            }
            
            // 叶子节点, replacement为空
            afterRemove(node: node, replacement: nil)

        } else { // 度为1的节点 找到左节点 或者右节点
            let replacement = node.left != nil ? node.left : node.right
            replacement?.parent = node.parent
            
            if node.isLeftChild {
                node.parent?.left = replacement
            } else if node.isRightChild {
                node.parent?.right = replacement
            }
            
            afterRemove(node: node, replacement: replacement)
        }
    }
    
    public func contains(element: T) -> Bool {
        return (node(element: element) != nil)
    }
    
    private func node(element: T) -> Node<T>? {
        var node: Node? = root
        while node != nil {
            if node!.element < element {
                node = node?.right
            } else if node!.element > element {
                node = node?.left
            } else {
                return node
            }
        }
        return nil
    }
}

