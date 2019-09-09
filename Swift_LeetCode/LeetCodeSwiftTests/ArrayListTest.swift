//
//  ArrayListTest.swift
//  LeetCodeSwiftTests
//
//  Created by Yang Yu on 2019/9/6.
//  Copyright © 2019 YangYu. All rights reserved.
//

import XCTest
@testable import LeetCodeSwift


class ArrayListTest: XCTestCase {
    
    override func setUp() {
        // Put setup code here. This method is called before the invocation of each test method in the class.
    }

    override func tearDown() {
        // Put teardown code here. This method is called after the invocation of each test method in the class.
    }

    /// 测试增删改查
    func testArrayAdd() {
        var arr = ArrayList<Int>()

        arr.append(11)
        arr.append(22)
        arr.append(33)
        arr.append(44)
        arr.append(55)
        
        if let e = arr.get(0) {
            XCTAssertTrue(e == 11, "")
        }
        arr.insert(66, at: 0)
        arr.insert(77, at: arr.size)
        arr.remove(at: 1)
        arr.append(88)
        
        XCTAssertTrue(arr.size == 7, "")

        if let e = arr.get(1) {
            XCTAssertTrue(e == 22, "")
        }
        
        if let e = arr.get(arr.size - 1) {
            XCTAssertTrue(e == 88, "")
        }
        
        XCTAssertTrue(arr.contains(11) == false, "")
        XCTAssertTrue(arr.contains(22) == true, "")
        XCTAssertTrue(arr.isEmpty() == false, "")

        arr.removeAll()
        
        XCTAssertTrue(arr.isEmpty() == true, "")
        XCTAssertTrue(arr.contains(11) == false, "")
        XCTAssertTrue(arr.contains(22) == false, "")

    }
    
    /// 测试扩容
    func testExpansion() {
        var arr = ArrayList<Int>()

        for i in 0..<30 {
            arr.append(i)
        }
        
        XCTAssertTrue(arr.size == 30)
        XCTAssertTrue(arr.contains(0))
        XCTAssertTrue(arr.contains(29))
        
        print(arr)

        for i in (0..<20).reversed() {
            arr.remove(at: i)
        }
        arr.append(5555)
        print(arr)
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
        
        var arr = ArrayList<Person>()

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
    
    func testExample() {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
    }

    func testPerformanceExample() {
        // This is an example of a performance test case.
        self.measure {
            // Put the code you want to measure the time of here.
        }
    }

}
