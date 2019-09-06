//
//  ArrayList.swift
//  LeetCodeSwift
//
//  Created by Yang Yu on 2019/9/6.
//  Copyright © 2019 YangYu. All rights reserved.
//  Swift实现动态数组

struct ArrayList<T> {
    
    /// 动态数组size
    public func size() -> Int {
        return 0
    }
    
    /// 是否为空
    public func isEmpty() -> Bool {
        return false
    }
    
    /// 是否包含某个元素
    public func contains(element: T) -> Bool {
        return false
    }
    
    /// 获取某个位置的元素
    public func get(index: Int) -> T {
        return T.self as! T
    }
    
    /// 设置index位置的元素 返回之前该位置的元素
    public func set(index: Int, element: T) ->T {
        return T.self as! T
    }
    
    /// 往index位置插入元素
    public func insert(index: Int, element: T) {
        
    }
    
    /// 删除某个位置的元素
    public func remove(index: Int) ->T {
        return T.self as! T
    }
    
    /// 查看某个元素的位置
    public func indexOf(element: T) -> Int {
        return 0
    }
    
    /// 清空所以元素
    public func clear() {
        
    }
    
}
