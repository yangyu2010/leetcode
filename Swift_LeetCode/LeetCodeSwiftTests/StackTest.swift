//
//  StackTest.swift
//  LeetCodeSwiftTests
//
//  Created by Yang Yu on 2019/9/12.
//  Copyright © 2019 YangYu. All rights reserved.
//

import XCTest
@testable import LeetCodeSwift

class StackTest: XCTestCase {

    func testExample() {
       let stack = Stack<Int>()
        
        stack.clear()
        stack.push(element: 11)
        stack.push(element: 22)
        stack.push(element: 33)
        
        XCTAssert(stack.pop() == 33)
        XCTAssert(stack.isEmpty == false)
        XCTAssert(stack.size == 2)
        XCTAssert(stack.top() == 22)

        stack.clear()
        XCTAssert(stack.isEmpty == true)
        XCTAssert(stack.size == 0)
        XCTAssert(stack.top() != 22)

        stack.push(element: 44)
        XCTAssert(stack.isEmpty == false)
        XCTAssert(stack.size == 1)
        XCTAssert(stack.top() == 44)
    }

    func testPerformanceExample() {
        // This is an example of a performance test case.
        self.measure {
            // Put the code you want to measure the time of here.
        }
    }

}
