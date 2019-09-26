//
//  AVLTree.swift
//  LeetCodeSwift
//
//  Created by Yang Yu on 2019/9/24.
//  Copyright © 2019 YangYu. All rights reserved.
//

class AVLNode<T>: Node<T> {
    
    private var height = 1
    
    var balanceFactor: Int {
        let leftHeight = (left == nil) ? 0 : (left as! AVLNode).height
        let rightHeight = (right == nil) ? 0 : (right as! AVLNode).height
        
        return leftHeight - rightHeight
    }
    
    var tallerChild: Node<T>? {
        let leftHeight = (left == nil) ? 0 : (left as! AVLNode).height
        let rightHeight = (right == nil) ? 0 : (right as! AVLNode).height
        if leftHeight < rightHeight {
            return right
        }
        if leftHeight > rightHeight {
            return left
        }
        return isLeftChild ? left : right
    }
    
    func updateHeight() {
        let leftHeight = (left == nil) ? 0 : (left as! AVLNode).height
        let rightHeight = (right == nil) ? 0 : (right as! AVLNode).height
        height = max(leftHeight, rightHeight) + 1
    }
}


class AVLTree<T: Comparable>: BinarySearchTree<T> {
    
    private func isBalanced(_ node: Node<T>?) -> Bool {
        if node == nil { return true }
        return abs((node as! AVLNode).balanceFactor) <= 1
    }
    
    override func creatNode(element: T, parent: Node<T>?) -> Node<T> {
        return AVLNode(element: element, parent: parent)
    }
    
    override func afterAdd(node: Node<T>?) {
        if node == nil {
            return
        }
        var cur = node!.parent
        while cur != nil {
            if isBalanced(cur) {
                (cur as! AVLNode).updateHeight()
                cur = cur?.parent
            } else {
                // 恢复平衡
                rebalance(cur)
                break
            }
        }
    }
    
    private func rebalance(_ grand: Node<T>?) {
        if grand == nil { return }
        guard let parent = (grand as! AVLNode).tallerChild else { return }
        guard let node = (parent as! AVLNode).tallerChild else { return }
        if parent.isLeftChild {
            if node.isLeftChild {
                // LL
                rotateRight(grand)
            } else {
                // LR
                rotateLeft(parent)
                rotateRight(grand)
            }
        } else {
            if node.isLeftChild {
                // RL
                rotateRight(parent)
                rotateLeft(grand)
            } else {
                // RR
                rotateLeft(grand)
            }
        }
    }

    private func rotateLeft(_ node: Node<T>?) {
        guard let node = node else { return }
        let root = node.right
        node.right = root?.left
        root?.left = node
        
        if node.isLeftChild {
            node.parent?.left = root
        } else if node.isRightChild {
            node.parent?.right = root
        } else {
            self.root = root
        }
        
        root?.parent = node.parent
        node.parent = root
        node.left?.parent = node
        node.right?.parent = node

        (node as! AVLNode).updateHeight()
        (root as! AVLNode).updateHeight()
    }
    
    private func rotateRight(_ node: Node<T>?) {
        guard let node = node else { return }
        let root = node.left
        node.left = root?.right
        root?.right = node
        
        if node.isLeftChild {
            node.parent?.left = root
        } else if node.isRightChild {
            node.parent?.right = root
        } else {
            self.root = root
        }
        
        root?.parent = node.parent
        node.parent = root
        node.right?.parent = node
        node.left?.parent = node

        (node as! AVLNode).updateHeight()
        (root as! AVLNode).updateHeight()
    }
    
    private func afterRotate(_ node: Node<T>?, root: Node<T>?) {
        
    }
}
