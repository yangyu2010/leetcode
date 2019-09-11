//
//  LinkedListTest.swift
//  LeetCodeSwiftTests
//
//  Created by Yang Yu on 2019/9/9.
//  Copyright © 2019 YangYu. All rights reserved.
//

import XCTest
@testable import LeetCodeSwift


class LinkedListTest: XCTestCase {

    /// 测试增删改查
    func testLinkedListAdd() {
//        let arr = LinkedList<Int>()
        let arr = DoubleLinkedList<Int>()
        
        arr.append(11)
        arr.append(22)
        arr.append(33)
        arr.append(44)
        arr.append(55)
        
        if let e = arr.get(0) {
            XCTAssertTrue(e == 11, "")
        }
        
        print(arr)
        if let e = arr.get(4) {
            XCTAssertTrue(e == 55, "")
        }
        
        arr.insert(66, at: 0)
        arr.insert(77, at: arr.size)
        arr.remove(at: 1)
        arr.append(88)
        
        // [66, 22, 33, 44, 55, 77, 88]
        XCTAssertTrue(arr.size == 7, "")
        
        if let e = arr.get(0) {
            XCTAssertTrue(e == 66, "")
        }
        if let e = arr.get(arr.size - 1) {
            XCTAssertTrue(e == 88, "")
        }
        if let e = arr.get(1) {
            XCTAssertTrue(e == 22, "")
        }

        XCTAssert(arr.indexOf(88) == 6)
        XCTAssert(arr.indexOf(66) == 0)
        
        print(arr)
        // [66, 22, 33, 44, 55, 77, 88]
        XCTAssert(arr.remove(at: 2) == 33)

        // [66, 22, 44, 55, 77, 88]
        XCTAssert(arr.indexOf(88) == 5)
        XCTAssert(arr.indexOf(66) == 0)
        XCTAssert(arr.indexOf(33) == -1)

        XCTAssert(arr.set(0, element: 111) == 66)
        XCTAssert(arr.set(5, element: 99) == 88)

        // [111, 22, 44, 55, 77, 99]
        XCTAssert(arr.get(0) == 111)
        XCTAssert(arr.get(5) == 99)
        
        XCTAssert(arr.remove(at: 0) == 111)
        
        XCTAssertTrue(arr.contains(11) == false, "")
        XCTAssertTrue(arr.contains(22) == true, "")
        XCTAssertTrue(arr.isEmpty == false, "")

        arr.removeAll()

        XCTAssertTrue(arr.isEmpty == true, "")
        XCTAssertTrue(arr.contains(11) == false, "")
        XCTAssertTrue(arr.contains(22) == false, "")
        
        arr.insert(33, at: 0)
        arr.insert(44, at: 0)
        arr.insert(11, at: 1)
        arr.insert(22, at: 2)
//        44 11 22 33
        XCTAssertTrue(arr.get(1) == 11, "")
        XCTAssertTrue(arr.get(0) == 44, "")
        XCTAssertTrue(arr.get(3) == 33, "")
        XCTAssertTrue(arr.get(2) == 22, "")

    }

    
    class Person: NSObject {
        var name: String?
        var age: Int = 0
        
        deinit {
            print((name ?? "没有name") + " " + "\(age)的Person被销毁了")
        }
    }
    
    /// 测试扩容
    func testExpansion2() {
        //        2 2 4 8 16 32
        //        var array: [Int] = []
        //        for i in 1...100 {
        //            array.append(i)
        //            let arrayPtr = UnsafeMutableBufferPointer<Int>(start: &array, count: array.count)
        //            print(arrayPtr)
        //        }
        
        let arr = LinkedList<Person>()
        
        for i in 0..<30 {
            let p = Person()
            p.age = i
            p.name = "name_\(i)"
            
            arr.append(p)
        }
        
        arr.removeAll()
        
        //        for i in (0..<20).reversed() {
        //            arr.remove(at: i)
        //        }
        
        print(arr)
    }
}
