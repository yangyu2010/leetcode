//
//  Stack.swift
//  LeetCodeSwift
//
//  Created by Yang Yu on 2019/9/12.
//  Copyright © 2019 YangYu. All rights reserved.
//  栈

struct Stack<T: Equatable> {
    private let list: DoubleLinkedList<T>
    
    init() {
        list = DoubleLinkedList<T>()
    }
    
    public var size: Int {
        return list.size
    }
    
    /// 是否为空
    public var isEmpty: Bool {
        return list.size == 0
    }
    
    /// 入栈
    public func push(element: T) {
        list.append(element)
    }
    
    /// 出栈
    public func pop() -> T? {
        return list.remove(at: list.size - 1)
    }
    
    /// 顶部元素
    public func top() -> T? {
        return list.get(list.size - 1)
    }
    
    /// 清空
    public func clear() {
        list.removeAll()
    }
}
