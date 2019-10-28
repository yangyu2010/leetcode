//
//  RBTreeTest.swift
//  LeetCodeSwiftTests
//
//  Created by YangYu on 2019/10/17.
//  Copyright © 2019 YangYu. All rights reserved.
//

import XCTest
@testable import LeetCodeSwift

class RBTreeTest: XCTestCase {

    func testExample() {
        
        let tree = RBTree<Int>()

        for aNum in [39, 93, 84, 60, 74, 64, 7, 67, 3, 78, 37, 76, 89, 100, 50, 80] {
            tree.add(element: aNum)
        }
        tree.remove(element: 78)
        tree.remove(element: 80)
        tree.remove(element: 7)

        tree._print()
        print("\n\n")
        
        
//        for aNum in [39, 93, 84, 60, 74, 64, 7, 67, 3, 78, 37, 76, 89, 100, 50, 80].reversed() {
//            tree.remove(element: aNum)
//            print("\n\n")
//        }
        
    }

    func testExample2() {
        
        let tree = RBTree<Int>()
        let arr = [57, 8, 88, 77, 27, 94, 67, 5, 38, 95,72, 81, 77, 64, 11, 45, 65, 56, 53, 19, 86, 62, 59]
        for aNum in arr {
            tree.add(element: aNum)
        }
        
        tree._print()

        
//        for aNum in arr {
//            tree.remove(element: aNum)
//        }
//
//        for aNum in arr.reversed() {
//            tree.add(element: aNum)
//        }
//
//        for aNum in arr {
//            tree.remove(element: aNum)
//        }
        
    }
}
