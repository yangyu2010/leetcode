//
//  Queue.swift
//  LeetCodeSwift
//
//  Created by Yang Yu on 2019/9/12.
//  Copyright © 2019 YangYu. All rights reserved.
//

struct Queue<T: Equatable> {
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
    
    /// 入栈
    public mutating func enQueue(element: T) {
        list.append(element)
    }
    
    /// 出栈
    public mutating func deQueue() -> T? {
        return list.remove(at: 0)
    }
    
    /// 顶部元素
    public func front() -> T? {
        return list.get(0)
    }
    
    /// 清空
    public mutating func clear() {
        list.removeAll()
    }
}
