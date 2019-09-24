//
//  BinarySearchTreeTest.swift
//  LeetCodeSwiftTests
//
//  Created by Yang Yu on 2019/9/24.
//  Copyright © 2019 YangYu. All rights reserved.
//

import XCTest
@testable import LeetCodeSwift

class BinarySearchTreeTest: XCTestCase {

    func testExample() {

        let tree = BinarySearchTree<Int>()

        for aNum in [19,
                  77,
                  81,
                  99,
                  49,
                  3,
                  19,
                  24,
                  57,
                  63,] {
                    tree.add(element: aNum)
        }
//        for _ in 0..<10 {
//            let aNum = Int(arc4random() % 100)
//            print(aNum)
//            tree.add(element: aNum)
//        }
        
//        tree.add(element: 11)
//        tree.add(element: 22)
//        tree.add(element: 33)
//        tree.add(element: 44)

        tree._print()
        
        tree.remove(element: 63)
        tree._print()
        
        tree.remove(element: 49)
        tree._print()

        tree.remove(element: 24)
        tree._print()
        
        tree.remove(element: 77)
        tree._print()

        XCTAssert(tree.contains(element: 77) == false)
        XCTAssert(tree.contains(element: 19) == true)
        XCTAssert(tree.contains(element: 3) == true)
        XCTAssert(tree.contains(element: 33) == false)

    }
}
