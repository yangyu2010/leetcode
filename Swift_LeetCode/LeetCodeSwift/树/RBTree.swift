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
    
    private var isBlack: Bool {
        return color == BLACK
    }

    private var isRed: Bool {
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
                    return ("\($0.element)" + " (" + parentString + ")" + "(" + colorString + ")" ,$0.left, $0.right)
                }
            }
            return ("\($0.element)" + " (" + parentString + ")" ,$0.left, $0.right)
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
     
     二叉树描述
     
        2(BLACK)         4(BLACK)         7(BLACK)      8(BLACK)
         /    \               \             /
        /      \               \           /
     1(RED)     3(RED)         5(RED)     6(RED)
     
     
     1. parent是黑色, 总共有4种情况, 不做处理
        ---(加在4的左边, 7的右边, 8的左右两边)
     
     2. parent是红色, uncle是红色, 总共有4种情况, 统一处理(B-tree中的上溢)
        ---(加在1的左右两边, 加在3的左右两边)

        parent = BLACK,
        uncle = BLACK,
        grand = RED, 同时再去 check grand
        若上溢到根结点, 把根结点染黑即可

     3. parent是红色, uncle是黑色, 总共有4种情况, 分别处理 (LL RR LR RL)
        ---(加在5的左右两边, 加在6的左右两边)

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
        guard let rbNode = node as? RBTreeNode else { return }
        guard let parent = rbNode.parent as? RBTreeNode else {
            colorBalck(node)
            return
        }
        
        // 分类1
        if isBlack(parent) {
            return
        }
        
        // 分类2 uncle是红色 表示uncle肯定有值
        let grand = parent.parent
        if let uncle = parent.sibling as? RBTreeNode,
            isRed(uncle) {
            colorBalck(parent)
            colorBalck(uncle)
            colorRed(grand)
            afterAdd(node: grand)
            // 若上溢到根结点, 把根结点染黑即可
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

    
    // MARK:- 删除后处理
    
    override func afterRemove(node: Node<T>?, replacement: Node<T>?) {
    
        guard let rbNode = node as? RBTreeNode else { return }
        
        
        /**
         真正删除的节点只会在下面的情况中产生
         
         二叉树描述
         
                2(BLACK)         4(BLACK)         7(BLACK)      8(BLACK)
               /    \               \             /
              /      \               \           /
          1(RED)     3(RED)         5(RED)     6(RED)
         
         
         B-Tree 描述
         
         123 34 67 8
         RBR BR RB B
         
         1. 删除的是红色, 直接删除
            ---(1 3 5 6)
         
         2. 删除的是黑色
            2.1 如果node有2个红色子节点
                ---(2)
                不可能直接被删除, 因为会找到它的子节点代替
                因为不考虑这种情况
            2.2 如果node有1个红色子节点
                ---(4 7)
                把子节点染成黑色 replacement = BLACK
            2.3 如果node节点没有红色子节点
                ---(8)
                2.3.1 兄弟节点是黑色
                      2.3.1.1 兄弟节点至少有1个红色子节点
                      2.3.1.2 兄弟节点没有红色子节点
                2.3.2 兄弟节点是红色
                      sibling = BLACK
                      parent = RED
                      parent 右旋转
                      sibling = paren.left
         */
        
        // 1.删除的是红色, 不处理
        if rbNode.color == RED {
            return
        }
        
        // 2.删除的是黑色
        // 2.1 不处理
        
        // 2.2 如果replacement存在, 且为红色, 说明node是度为1的节点, 把替换的节点染黑色即可
        if let rbReplacement = replacement as? RBTreeNode,
            rbReplacement.color == RED {
            colorBalck(rbReplacement)
            return
        }
        
        
        // 2.3 删除的是黑色, 同时也是叶子节点
        
        // node是根结点 直接返回
        guard let parent = rbNode.parent as? RBTreeNode else { return }
        
        // 先看自己是 left 还是 right
        let isLeftChild = parent.left == nil || parent.left!.isLeftChild
        guard var sibling = (isLeftChild ? parent.right : parent.left) as? RBTreeNode else {
            print("---------Warning---- sibling节点为空 没有处理")
            return
        }
        if isLeftChild { //被删除的在左边, 兄弟节点在右边
            // 2.3.2 兄弟节点是红色
            if isRed(sibling) {
                colorBalck(sibling)
                colorRed(parent)
                rotateLeft(parent)
                sibling = parent.right as! RBTreeNode<T>
            }
            
            // 2.3.1 兄弟节点是黑色
            
            if isBlack(sibling.left) && isBlack(sibling.right) {
                // 2.3.1.2 兄弟节点没有红色子节点 父节点向下跟兄弟节点合并
                let parentIsBlack = parent.color == BLACK
                colorRed(sibling)
                colorBalck(parent)
                
                // 如果父节点是黑色, 需要对父节点再次 check
                if parentIsBlack {
                    afterRemove(node: parent, replacement: nil)
                }
            } else {
                // 2.3.1.1 兄弟节点至少有1个红色子节点 向兄弟节点借元素
                if isBlack(sibling.right) {
                    rotateRight(sibling)
                    sibling = parent.right as! RBTreeNode<T>
                }
                
                color(sibling, color: parent.color)
                colorBalck(sibling.right)
                colorBalck(parent)
                rotateLeft(parent)
            }
        } else { //被删除的在右边, 兄弟节点在左边
            // 2.3.2 兄弟节点是红色
            if isRed(sibling) {
                colorBalck(sibling)
                colorRed(parent)
                rotateRight(parent)
                sibling = parent.left as! RBTreeNode<T>
            }
            
            // 2.3.1 兄弟节点是黑色

            if isBlack(sibling.left) && isBlack(sibling.right) {
                // 2.3.1.2 兄弟节点没有红色子节点 父节点向下跟兄弟节点合并
                let parentIsBlack = parent.color == BLACK
                colorRed(sibling)
                colorBalck(parent)
                
                // 如果父节点是黑色, 需要对父节点再次 check
                if parentIsBlack {
                    afterRemove(node: parent, replacement: nil)
                }
            } else {
                // 2.3.1.1 兄弟节点至少有1个红色子节点 向兄弟节点借元素
                if isBlack(sibling.left) {
                    rotateLeft(sibling)
                    sibling = parent.left as! RBTreeNode<T>
                }
                
                color(sibling, color: parent.color)
                colorBalck(sibling.left)
                colorBalck(parent)
                rotateRight(parent)
            }
        }
        
    }
  
    
    // MARK:- 旋转
    // 旋转和 AVL 树一样, 区别在于, AVL旋转后需要更新高度, 红黑树不用
    
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

    private func isBlack(_ node: Node<T>?) -> Bool {
        if let rbNode = node as? RBTreeNode {
            return rbNode.color == BLACK
        }
        return true
    }
    
    private func isRed(_ node: Node<T>?) -> Bool {
        if let rbNode = node as? RBTreeNode {
            return rbNode.color == RED
        }
        return false
    }
    
    @discardableResult
    private func colorBalck(_ node: Node<T>?) -> Node<T>? {
        return color(node, color: BLACK)
    }
    
    @discardableResult
    private func colorRed(_ node: Node<T>?) -> Node<T>? {
        return color(node, color: RED)
    }
    
    @discardableResult
    private func color(_ node: Node<T>?, color: Bool) -> Node<T>? {
        if let rbNode = node as? RBTreeNode {
            rbNode.color = color
            return rbNode
        } else {
            return nil
        }
    }
}

