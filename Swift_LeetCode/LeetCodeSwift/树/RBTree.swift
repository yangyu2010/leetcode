//
//  RBTree.swift
//  LeetCodeSwift
//
//  Created by YangYu on 2019/10/17.
//  Copyright © 2019 YangYu. All rights reserved.
//  红黑树


let RED: Bool = true
let BLACK: Bool = false

class RBTreeNode<T>: Node<T> {

    var color: Bool = RED
    
    var isBlack: Bool {
        return color == BLACK
    }

    var isRed: Bool {
        return color == RED
    }

    override var asString: String {
        return treeString(self as Node) {
            
            var parentString = "null"
            if $0.parent != nil {
                parentString = "\($0.parent!.element)"
            }
            
            var colorString = ""
            if let rbNode = $0 as? RBTreeNode {
                if rbNode.isRed {
                    colorString = "红"
                } else {
                    colorString = "黑"
                }
            }
            return ("\($0.element)" + " (" + parentString + ")" + "(" + colorString + ")" ,$0.left, $0.right)
        }
    }
}


class RBTree<T: Comparable>: BinarySearchTree<T> {

    override func creatNode(element: T, parent: Node<T>?) -> Node<T> {
        return RBTreeNode(element: element, parent: parent)
    }
    
    //MARK:- 添加后处理
    
    /**
     添加总共有12种情况, 可以分3类
     1. parent是黑色, 总共有4种情况, 不做处理
     
     2. parent是红色, uncle是红色, 总共有4种情况, 统一处理
        parent = BLACK,
        uncle = BLACK,
        grand = RED, 同时再去 check grand
     
     3. parent是红色, uncle是黑色, 总共有4种情况, 分别处理 (LL RR LR RL)
        LL: parent = BLACK,
            grand = RED,
            grand 右旋转
        RR: parent = BLACK,
            grand = RED,
            grand 左旋转
        LR: self = BLACK
            grand = RED
            parent 左旋转, grand右旋转
        RL: self = BLACK
            grand = RED
            parent 右旋转, grand左旋转
     */
    override func afterAdd(node: Node<T>?) {
        guard let rbNode = node else { return }
        guard let parent = rbNode.parent as? RBTreeNode else {
            colorBalck(node)
            return
        }
        
        // 分类1
        if parent.isBlack {
            return
        }
        
        // 分类2 uncle是红色 表示uncle肯定有值
        let grand = parent.parent
        if let uncle = parent.sibling as? RBTreeNode,
            uncle.isRed {
            colorBalck(parent)
            colorBalck(uncle)
            colorRed(grand)
            afterAdd(node: grand)
            return
        }
        
        // 分类3
        if parent.isLeftChild {
            if rbNode.isLeftChild {
                // LL
                colorBalck(parent)
                colorRed(grand)
                
                rotateRight(grand)
            } else {
                // LR
                colorBalck(rbNode)
                colorRed(grand)
                
                rotateLeft(parent)
                rotateRight(grand)
            }
        } else {
            if rbNode.isLeftChild {
                // RL
                colorBalck(rbNode)
                colorRed(grand)
                
                rotateRight(parent)
                rotateLeft(grand)
            } else {
                // RR
                colorBalck(parent)
                colorRed(grand)
                
                rotateLeft(grand)
            }
        }
    }

    
    //MARK:- 删除后处理
    
    override func afterRemove(node: Node<T>?) {
        
    }
  
    
    //MARK:- 旋转
    
    private func rotateLeft(_ node: Node<T>?) {
        guard let node = node else { return }
        guard let root = node.right else { return }
        node.right = root.left
        root.left = node
        
        afterRotate(node, root: root)
    }
    
    private func rotateRight(_ node: Node<T>?) {
        guard let node = node else { return }
        guard let root = node.left else { return }
        node.left = root.right
        root.right = node
        
        afterRotate(node, root: root)
    }
    
    private func afterRotate(_ node: Node<T>, root: Node<T>) {
        if node.isLeftChild {
            node.parent?.left = root
        } else if node.isRightChild {
            node.parent?.right = root
        } else {
            self.root = root
        }
        
        root.parent = node.parent
        node.parent = root
        node.right?.parent = node
        node.left?.parent = node
        
//        (node as? AVLNode)?.updateHeight()
//        (root as? AVLNode)?.updateHeight()
    }
    
    
    //MARK:- 染色

    @discardableResult
    private func colorBalck(_ node: Node<T>?) -> Node<T>? {
        return color(node, color: BLACK)
    }
    
    @discardableResult
    private func colorRed(_ node: Node<T>?) -> Node<T>? {
        return color(node, color: RED)
    }
    
    private func color(_ node: Node<T>?, color: Bool) -> Node<T>? {
        if let rbNode = node as? RBTreeNode {
            rbNode.color = color
            return rbNode
        } else {
            return nil
        }
    }
}

