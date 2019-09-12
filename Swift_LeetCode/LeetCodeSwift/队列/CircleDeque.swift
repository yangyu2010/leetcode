//
//  CircleDeque.swift
//  LeetCodeSwift
//
//  Created by Yang Yu on 2019/9/12.
//  Copyright © 2019 YangYu. All rights reserved.
//  双端循环队列(没有优化)

struct CircleDeque<T: Equatable> {
    /// 默认创建数组的大小
    private let DEFAULT_CAPACITY: Int = 10
    /// 内部保存元素的数组
    private var elements: [T?]
    
    /// 头下标
    private var front: Int = -1
    /// 尾下标
    private var rear: Int = -1
    
    init() {
        elements = [T?](repeating: nil, count: DEFAULT_CAPACITY)
    }
    
    /// 获取某个位置的前一个
    private func getPrevIndex(_ index: Int) -> Int {
        if index < 0 {
            return 0
        }
        return (index - 1 + elements.count) % elements.count
    }
    
    /// 获取某个位置的后一个
    private func getNextIndex(_ index: Int) -> Int {
        return (index + 1) % elements.count
    }
    
    /// arrayList的size
    private(set) var size: Int = 0

    /// 是否为空
    public var isEmpty: Bool {
        return size == 0
    }
    
    /// 从队头入队
    public mutating func enQueueFront(element: T) {
        // 第一次加入时,
        if rear == -1 {
            rear = 0
        }
        front = getPrevIndex(front)
        elements[front] = element
        size += 1
    }
    
    /// 从队尾入队
    public mutating func enQueueRear(element: T) {
        // 第一次加入时,
        if front == -1 {
            front = 0
        }
        rear = getNextIndex(rear)
        elements[rear] = element
        size += 1
    }
    
    /// 从队头出队
    @discardableResult
    public mutating func deQueueFront() -> T? {
        let e = elements[front]
        elements[front] = nil
        front = getNextIndex(front)
        size -= 1
        if size == 0 {
            front = -1
            rear = -1
        }
        return e
    }
    
    /// 从队尾出队
    @discardableResult
    public mutating func deQueueRear() -> T? {
        let e = elements[rear]
        elements[rear] = nil
        rear = getPrevIndex(rear)
        size -= 1
        if size == 0 {
            front = -1
            rear = -1
        }
        return e
    }
    
    /// 顶部元素
    public func getFront() -> T? {
        return elements[front]
    }
    
    /// 尾部元素
    public func getRear() -> T? {
        return elements[rear]
    }
    
    /// 清空
    public mutating func clear() {
        size = 0
        front = -1
        rear = -1
        
        for i in 0..<elements.count {
            elements[i] = nil
        }
    }
}
