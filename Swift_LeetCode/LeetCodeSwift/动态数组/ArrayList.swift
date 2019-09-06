//
//  ArrayList.swift
//  LeetCodeSwift
//
//  Created by Yang Yu on 2019/9/6.
//  Copyright © 2019 YangYu. All rights reserved.
//  Swift实现动态数组

public struct ArrayList<T: Equatable> {

    public enum ArrayListError: Error {
        case indexOutOfBounds
    }
    
    /// 元素没有找到返回值
    public let ELEMENT_NOT_FOUND: Int = -1
    /// 默认创建数组的大小
    private let DEFAULT_CAPACITY: Int = 10
    /// 内部保存元素的数组
    private var elements: [T?]
    /// arrayList的size
    private(set) var size: Int = 0

    public init(capaticy: Int) {
        if capaticy < DEFAULT_CAPACITY {
            elements = [T?](repeating: nil, count: DEFAULT_CAPACITY)
        } else {
            elements = [T?](repeating: nil, count: capaticy)
        }
    }
    
    public init() {
        elements = [T?](repeating: nil, count: DEFAULT_CAPACITY)
    }
    
    var description: String {
        var str = ""
        for e in elements {
            str += e.debugDescription
        }
        return str
    }
    
    /// 检查index(查询, 移除时)
    private func checkIndex(_ index: Int) throws {
        if index < 0 || index > size - 1 {
            throw ArrayListError.indexOutOfBounds
        }
    }
    
    /// 检查index(插入时)
    private func checkIndexForAdd(_ index: Int) throws {
        if index < 0 || index > size {
            throw ArrayListError.indexOutOfBounds
        }
    }
    
    /// 是否为空
    public func isEmpty() -> Bool {
        return size == 0
    }
    
    /// 是否包含某个元素
    public func contains(_ element: T) -> Bool {
        return indexOf(element) != ELEMENT_NOT_FOUND
    }
    
    /// 添加元素
    public mutating func add(_ element: T) {
        /**
         这里不能用append()
         elements.append(element)
         系统会自动扩容, 添加到尾部
         */
        elements[size] = element
        size += 1
    }
    
    /// 获取某个位置的元素
    public func get(_ index: Int) -> T? {
        try! checkIndex(index)
        return elements[index]
    }
    
    /// 设置index位置的元素 返回之前该位置的元素
    public mutating func set(_ index: Int, element: T) ->T? {
        try! checkIndex(index)
        let old_element = elements[index]
        elements[index] = element
        return old_element
    }
    
    /// 往index位置插入元素
    public mutating func insert(_ element: T, at index: Int) {
        try! checkIndexForAdd(index)
        
        /*
         0  1  2  3  4
         [11 22 33 44 55 nil nil nil nil nil]
         在1的位置插入 66
         [11 66 22 33 44 55 nil nil nil nil]
         需要把1-4(index-size)的元素往后移动
        **/
        for i in (index..<size).reversed() {
            elements[i+1] = elements[i]
        }
        elements[index] = element
        size += 1
    }
    
    /// 删除某个位置的元素
    @discardableResult
    public mutating func remove(at index: Int) ->T? {
        try! checkIndex(index)
        
        /*
         0  1  2  3  4
         [11 22 33 44 55 nil nil nil nil nil]
         删除1的位置
         [11 66 22 33 44 55 nil nil nil nil]
         需要把2-4((index+1)-size)的元素往前移动
         **/
        let old_element = elements[index]
        for i in (index + 1)...size {
            elements[i-1] = elements[i]
        }
        size -= 1
        return old_element
    }
    
    /// 查看某个元素的位置
    public func indexOf(_ element: T) -> Int {
        for (index, item) in elements.enumerated() {
            if item != nil && item! == element {
                return index
            }
        }
        return ELEMENT_NOT_FOUND
    }
    
    /// 清空所以元素
    public mutating func removeAll() {
        size = 0
    }
    
}
