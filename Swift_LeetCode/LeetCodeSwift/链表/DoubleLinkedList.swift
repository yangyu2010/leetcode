//
//  DoubleLinkedList.swift
//  LeetCodeSwift
//
//  Created by Yang Yu on 2019/9/11.
//  Copyright © 2019 YangYu. All rights reserved.
//  双向链表


public class DoubleLinkedList<T: Equatable> {
    
    /// 元素没有找到返回值
    public let ELEMENT_NOT_FOUND: Int = -1
    /// arrayList的size
    private(set) var size: Int = 0
    private var head: ListNode<T>?
    private var tail: ListNode<T>?

    /// 检查index(查询, 移除时)
    private func checkIndex(_ index: Int) throws {
        if index < 0 || index > size - 1 {
            throw ListError.indexOutOfBounds
        }
    }
    
    /// 检查index(插入时)
    private func checkIndexForAdd(_ index: Int) throws {
        if index < 0 || index > size {
            throw ListError.indexOutOfBounds
        }
    }
    
    /// 获取某个下标的node
    private func node(of index: Int) -> ListNode<T>? {
        do {
            try checkIndex(index)
        } catch {
            print("node of action error")
            return nil
        }
        
        if index < (size >> 1) {
            var curNode = head
            for _ in 0..<index {
                curNode = curNode?.next
            }
            return curNode
        } else {
            var curNode = tail
            for _ in index..<size-1 {
                curNode = curNode?.prev
            }
            return curNode
        }
    }
    
    /// 是否为空
    public var isEmpty: Bool {
        return size == 0
    }
    
    /// 是否包含某个元素
    public func contains(_ element: T) -> Bool {
        return indexOf(element) != ELEMENT_NOT_FOUND
    }
    
    /// 添加元素
    public func append(_ element: T) {
        insert(element, at: size)
    }
    
    /// 获取某个位置的元素
    public func get(_ index: Int) -> T? {
        do {
            try checkIndex(index)
        } catch {
            print("get action error")
            return nil
        }
        return node(of: index)?.element
    }
    
    /// 设置index位置的元素 返回之前该位置的元素
    public func set(_ index: Int, element: T) ->T? {
        try! checkIndexForAdd(index)
        if index == 0 {
            let origin = head?.element
            head?.element = element
            return origin
        } else {
            guard let cur = node(of: index) else { return nil }
            let origin = cur.element
            cur.element = element
            return origin
        }
    }
    
    /// 往index位置插入元素
    public func insert(_ element: T, at index: Int) {
        try! checkIndexForAdd(index)
        
        if index == 0 {
            // 0的位置
            let next = head
            head = ListNode(element: element)
            head?.next = next
            next?.prev = head
            if tail == nil {
                tail = head
            }
        } else {
            if let next = node(of: index) {
                // 其他中间位置
                let prev = next.prev
                let cur = ListNode(element: element, next: next, prev: prev)
                
                next.prev = cur
                prev?.next = cur
            } else {
                // 没有该位置的 表示是最后的位置插入
                let prev = tail
                let cur = ListNode(element: element, next: nil, prev: prev)
                prev?.next = cur
                tail = cur
            }
        }
        size += 1
    }
    
    /// 删除某个位置的元素
    @discardableResult
    public func remove(at index: Int) ->T? {
        try! checkIndex(index)
        
        if index == 0 {
            let element = head?.element
            head = head?.next
            size -= 1
            return element
        } else {
            guard let node = node(of: index) else { return nil }
            let prev = node.prev
            let next = node.next
            prev?.next = next
            next?.prev = prev
            size -= 1
            if node === tail {
                tail = prev
            }
            return node.element
        }
    }
    
    /// 查看某个元素的位置
    public func indexOf(_ element: T) -> Int {
        
        var node = head
        var index = 0
        while node != nil {
            if node!.element == element {
                return index
            }
            node = node!.next
            index += 1
        }
        
        return ELEMENT_NOT_FOUND
    }
    
    /// 清空所以元素
    public func removeAll() {
        //        var node = head
        //        while node != nil {
        //            node = node?.next
        //        }
        head = nil
        tail = nil
        size = 0
    }
}


extension DoubleLinkedList: CustomStringConvertible {
    public var description: String {
        var desc = "["
        var node = head
        while node != nil {
            desc += (node?.description ?? "no description")
            desc += ", "
            node = node!.next
        }
        desc += "]"
        return desc
    }
}
