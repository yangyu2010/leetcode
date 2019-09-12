//
//  QueueTest.swift
//  LeetCodeSwiftTests
//
//  Created by Yang Yu on 2019/9/12.
//  Copyright © 2019 YangYu. All rights reserved.
//

import XCTest
@testable import LeetCodeSwift

class QueueTest: XCTestCase {

    func testExample() {
        var q = Queue<Int>()
        
        q.clear()
        q.enQueue(element: 11)
        q.enQueue(element: 22)
        q.enQueue(element: 33)
        
        XCTAssert(q.deQueue() == 11)
        XCTAssert(q.isEmpty == false)
        XCTAssert(q.size == 2)
        XCTAssert(q.deQueue() == 22)
        XCTAssert(q.front() == 33)

        q.clear()
        XCTAssert(q.isEmpty == true)
        XCTAssert(q.size == 0)
//        XCTAssert(q.deQueue() != 22)
        
        q.enQueue(element: 44)
        XCTAssert(q.front() == 44)
        XCTAssert(q.isEmpty == false)
        XCTAssert(q.size == 1)
        XCTAssert(q.deQueue() == 44)
        
    }

    
    func testDeque() {
        var q = Deque<Int>()
        
        q.clear()
        XCTAssert(q.isEmpty == true)
        XCTAssert(q.size == 0)
        
        q.enQueueFront(element: 11)
        q.enQueueRear(element: 22)
        q.enQueueFront(element: 33)
        q.enQueueRear(element: 44)
        q.enQueueFront(element: 55)
        q.enQueueRear(element: 66)
        
//        55 33 11 22 44 66
        XCTAssert(q.front() == 55)
        XCTAssert(q.rear() == 66)
        XCTAssert(q.isEmpty == false)
        XCTAssert(q.size == 6)
        
        print(q)
        
        XCTAssert(q.deQueueRear() == 66)
        XCTAssert(q.deQueueRear() == 44)
        XCTAssert(q.deQueueFront() == 55)
        XCTAssert(q.deQueueRear() == 22)
        XCTAssert(q.deQueueFront() == 33)
        XCTAssert(q.deQueueFront() == 11)

        for i in 0..<10 {
            q.enQueueFront(element: i + 1)
            q.enQueueRear(element: i + 100)
        }
        
        for _ in 0..<3 {
            q.deQueueFront()
            q.deQueueRear()
        }
        
        q.enQueueFront(element: 11)
        q.enQueueFront(element: 12)
        
        while !q.isEmpty {
            print(q.deQueueFront() ?? "no dequeue")
        }
    }

    
    func testCircleDeque() {
        var q = CircleDeque2<Int>()
        // [1, 100, 101, 102, 103, 0, 0, 4, 3, 2]
        for i in 0..<4 {
            q.enQueueFront(element: i + 1)
            q.enQueueRear(element: i + 100)
        }
        
        XCTAssert(q.getFront() == 4)
        XCTAssert(q.getRear() == 103)
        XCTAssert(q.size == 8)

        // [1, 100, 0, 0, 0, 0, 0, 0, 0, 0]

        for _ in 0..<3 {
            q.deQueueFront()
            q.deQueueRear()
        }
        XCTAssert(q.getFront() == 1)
        XCTAssert(q.getRear() == 100)
        XCTAssert(q.size == 2)
        
        q.enQueueFront(element: 11)
        q.enQueueFront(element: 12)
        
        XCTAssert(q.getFront() == 12)
        XCTAssert(q.getRear() == 100)
        XCTAssert(q.size == 4)
        XCTAssert(q.isEmpty == false)

        q.deQueueRear()
        q.deQueueFront()
        q.deQueueFront()
        q.deQueueRear()
        
        q.clear()
        XCTAssert(q.isEmpty == true)
        XCTAssert(q.size == 0)

        q.enQueueRear(element: 111)
        XCTAssert(q.getFront() == 111)
        XCTAssert(q.getRear() == 111)

        q.deQueueFront()
        XCTAssert(q.isEmpty == true)
        XCTAssert(q.size == 0)

        
//        var q = CircleDeque<Int>()
//        q.enQueueRear(element: 11)
//        q.enQueueRear(element: 22)
//        q.enQueueRear(element: 33)
//
//        print(q)
//
//        XCTAssert(q.getRear() == 33)
//        XCTAssert(q.getFront() == 11)

        
//        q.enQueueFront(element: 11)
//        q.enQueueFront(element: 33)
//        q.enQueueRear(element: 44)
//        q.enQueueFront(element: 55)
//        q.enQueueRear(element: 66)
//
//        print(q)
//
//        q.deQueueFront()
//        q.deQueueFront()
//        q.deQueueFront()
    }
    
    
    func testCircleDeque2() {
        var q = CircleDeque2<Int>()
        
//         头10 9 8 7 6 5 4 3 2 1 100 101 102 103 104 105 106 107 108 109尾
        
        // 头5 4 3 2 1 100 101 102 103 104尾
        
        for i in 0..<10 {
            q.enQueueFront(element: i + 1)
            q.enQueueRear(element: i + 100)
        }
        
//        XCTAssert(q.getFront() == 10)
//        XCTAssert(q.getRear() == 109)
//
        print(q)
        
//        for _ in 0..<3 {
//            q.deQueueFront()
//            q.deQueueRear()
//        }
//
//        q.enQueueFront(element: 11)
//        q.enQueueFront(element: 12)
//
//        print(q)
//
        while !q.isEmpty {
            print(q.deQueueFront() ?? "no deq")
        }
    }
}
