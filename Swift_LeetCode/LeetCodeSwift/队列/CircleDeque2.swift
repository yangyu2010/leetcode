//
//  CircleDeque2.swift
//  LeetCodeSwift
//
//  Created by Yang Yu on 2019/9/12.
//  Copyright © 2019 YangYu. All rights reserved.
//  双端循环队列(优化后)

struct CircleDeque2<T: Equatable> {
    /// 默认创建数组的大小
    private let DEFAULT_CAPACITY: Int = 10
    /// 内部保存元素的数组
    private var elements: [T?]
    
    /// 头下标
    private var front: Int = 0

    init() {
        elements = [T?](repeating: nil, count: DEFAULT_CAPACITY)
    }
    
    /// 获取真实坐标
    private func index(_ index: Int) -> Int {
        var realIndex = index + front
        if realIndex < 0 {
            // 0的位置再往前
            realIndex += elements.count
        } else {
            realIndex = realIndex % elements.count
        }
        return realIndex
    }

    /// 扩容
    private mutating func ensureCapacity(capacity: Int) {
        let oldCapacity = elements.count
        if oldCapacity >= capacity {
            return
        }
        
        let newCapacity = oldCapacity + oldCapacity >> 1
        var newElements = [T?](repeating: nil, count: newCapacity)
        for i in 0..<size {
            newElements[i] = elements[index(i)]
        }
        elements = newElements
        front = 0
        print("-----------\(oldCapacity) 扩容为 \(newCapacity)---------")
    }
    
    /// 缩容
    private mutating func trim() {
        let oldCapacity = elements.count
        let newCapacity = oldCapacity >> 1
        
        // 当前capacity已经比默认的小了 return
        // 当前的使用量大于总容量的一半时 return
        if oldCapacity <= DEFAULT_CAPACITY ||
            size > newCapacity {
            return
        }
        
        var newElements = [T?](repeating: nil, count: newCapacity)
        for i in 0..<size {
            newElements[i] = elements[index(i)]
        }
        elements = newElements
        front = 0
        print("-----------\(oldCapacity) 缩容为 \(newCapacity)---------")
    }
    
    
    private(set) var size: Int = 0
    
    /// 是否为空
    public var isEmpty: Bool {
        return size == 0
    }
    
    /// 从队头入队
    public mutating func enQueueFront(element: T) {
        front = index(-1)
        elements[front] = element
        size += 1
    }
    
    /// 从队尾入队
    public mutating func enQueueRear(element: T) {
        ensureCapacity(capacity: size + 1)

        // 从front偏移size
        elements[index(size)] = element
        size += 1
    }
    
    /// 从队头出队
    @discardableResult
    public mutating func deQueueFront() -> T? {
        let e = elements[front]
        elements[front] = nil
        front = index(1)
        size -= 1
        trim()
        return e
    }
    
    /// 从队尾出队
    @discardableResult
    public mutating func deQueueRear() -> T? {
        let rearIndex = index(size - 1)
        let e = elements[rearIndex]
        elements[rearIndex] = nil
        size -= 1
        trim()
        return e
    }
    
    /// 顶部元素
    public func getFront() -> T? {
        return elements[front]
    }
    
    /// 尾部元素
    public func getRear() -> T? {
        return elements[index(size - 1)]
    }
    
    /// 清空
    public mutating func clear() {
        size = 0
        front = 0
        
        for i in 0..<size {
            elements[index(i)] = nil
        }
        
        trim()
    }
}


extension CircleDeque2: CustomStringConvertible {
    public var description: String {
        var desc = "["
        for i in 0..<size {
            if let e = elements[index(i)] {
                desc += "\(String(describing: e))"
            } else {
                desc += "no desc"
            }
            desc += ", "
        }
        desc += "]"
        return desc
    }
}

