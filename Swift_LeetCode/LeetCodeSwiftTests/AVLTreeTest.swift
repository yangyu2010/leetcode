//
//  AVLTreeTest.swift
//  LeetCodeSwiftTests
//
//  Created by Yang Yu on 2019/9/24.
//  Copyright © 2019 YangYu. All rights reserved.
//

import XCTest
@testable import LeetCodeSwift

class AVLTreeTest: XCTestCase {

    func testExample() {
        
        let tree = AVLTree<Int>()
        
        for aNum in [19,
                     77,
                     81,
                     16,
                     12,
                    10] {
                        tree.add(element: aNum)
                        tree._print()
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
        
        
        

        
    }

}
