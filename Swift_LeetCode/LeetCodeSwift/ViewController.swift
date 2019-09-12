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
        
//        testCircleDeque()
    }
    
    func testCircleDeque() {
        var q = CircleDeque<Int>()
        q.enQueueRear(element: 22)
        q.enQueueFront(element: 11)
        q.enQueueFront(element: 33)
        q.enQueueRear(element: 44)
        q.enQueueFront(element: 55)
        q.enQueueRear(element: 66)

        print(q)
        
        q.deQueueFront()
        q.deQueueFront()
        q.deQueueFront()
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
            arr.append(i)
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
        print(arr.contains(0))
        
    }
    
    
    class Person: NSObject {
        var name: String?
        var age: Int = 0
        
        deinit {
            print((name ?? "没有name") + " " + "\(age)的Person被销毁了")
        }
    }
    
    func testArrayList2() {
        
        var arr = ArrayList<Person>()
        
        for i in 0..<30 {
            let p = Person()
            p.age = i
            p.name = "name_\(i)"
            
            arr.append(p)
        }
        
//        arr.removeAll()
        
//        for i in (0..<30).reversed() {
//            arr.remove(at: i)
//        }
        
        print(arr)
    }
}

