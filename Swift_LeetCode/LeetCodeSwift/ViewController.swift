//
//  ViewController.swift
//  LeetCodeSwift
//
//  Created by Yang Yu on 2019/9/3.
//  Copyright © 2019 YangYu. All rights reserved.
//

import UIKit


class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        testArrayList()
        
//        var arr = Array<Int>()
//        arr.append(11)
//        arr.append(22)
//        arr.append(33)
//        arr.append(44)
//        arr.append(55)
//        print(arr)
//        arr.insert(66, at: 1)
//        print(arr[0])
        
    }

    func testArrayList() {
        var arr = ArrayList<Int>()

//        arr.add(11)
//        arr.add(22)
//        arr.add(33)
//        arr.add(44)
//        arr.add(55)
//
//        if let e = arr.get(0) {
//            print(e)
//        }
//        arr.insert(66, at: 0)
//
//        if let e = arr.get(0) {
//            print(e)
//        }
//
//        arr.insert(77, at: arr.size)
//        arr.insert(88, at: 0)
//
////        arr.insert(at: 0, element: 88)
//        print(arr)
//        arr.removeAll()
//        print(arr)
        
        
        for i in 0..<10 {
            print(i)
            arr.add(i)
        }
        
        print(arr)
        print("-----------------------------")
//        for i in 0..<10 {
//            print(i)
//            arr.remove(at: i)
//        }
        for i in (0..<10).reversed() {
            print(i)
            arr.remove(at: i)
        }
        
        print(arr)

    }
}

