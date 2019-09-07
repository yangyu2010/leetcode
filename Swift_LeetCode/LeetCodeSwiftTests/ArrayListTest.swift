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

    func testArrayAdd() {
        var arr = ArrayList<Int>()

        arr.add(11)
        arr.add(22)
        arr.add(33)
        arr.add(44)
        arr.add(55)
        
        if let e = arr.get(0) {
            XCTAssertTrue(e == 11, "")
        }
        arr.insert(66, at: 0)
        arr.insert(77, at: arr.size)
        arr.remove(at: 1)
        arr.add(88)
        
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
