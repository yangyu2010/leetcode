//
//  Deque.swift
//  LeetCodeSwift
//
//  Created by Yang Yu on 2019/9/12.
//  Copyright © 2019 YangYu. All rights reserved.
//  双端循环队列


struct Deque<T: Equatable> {
    private var list: ArrayList<T>
    
    init() {
        list = ArrayList<T>()
    }
    
    public var size: Int {
        return list.size
    }
    
    /// 是否为空
    public var isEmpty: Bool {
        return list.size == 0
    }
    
    /// 从队尾入队
    public mutating func enQueueRear(element: T) {
        list.append(element)
    }
    
    /// 从队头入队
    public mutating func enQueueFront(element: T) {
        list.insert(element, at: 0)
    }
    
    /// 从队尾出队
    @discardableResult
    public mutating func deQueueRear() -> T? {
        return list.remove(at: size - 1)
    }
    
    /// 从队头出队
    @discardableResult
    public mutating func deQueueFront() -> T? {
        return list.remove(at: 0)
    }
    
    /// 顶部元素
    public func front() -> T? {
        return list.get(0)
    }
    
    /// 尾部元素
    public func rear() -> T? {
        return list.get(size - 1)
    }
    
    /// 清空
    public mutating func clear() {
        list.removeAll()
    }
}
