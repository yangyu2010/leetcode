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
        
        tree._print()

//        tree.remove(element: 7)

//        for aNum in [19, 77, 81, 16, 12, 10, 17, 18, 20, 84, 82] {
//            tree.add(element: aNum)
//        }
        
        tree._print()
//        tree.remove(element: 82)
//        tree.remove(element: 20)
//        tree.remove(element: 77)
//
//        tree.remove(element: 84)
//        tree._print()
//
//        tree.remove(element: 16)
//
//        tree._print()
        
        //        for _ in 0..<10 {
        //            let aNum = Int(arc4random() % 100)
        //            print(aNum)
        //            tree.add(element: aNum)
        //        }
        
        //        tree.add(element: 11)
        //        tree.add(element: 22)
        //        tree.add(element: 33)
        //        tree.add(element: 44)
        
    }


}
