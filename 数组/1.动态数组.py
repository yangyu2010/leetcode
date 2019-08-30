#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Yu Yang


DEFAULT_CAPACITY = 5
ELEMENTS_NOT_FOUND = -1


class ArrayList:
    __size = 0

    def __init__(self, capacity=DEFAULT_CAPACITY):
        capacity = DEFAULT_CAPACITY if capacity < DEFAULT_CAPACITY else capacity
        self.__elements = [None] * capacity

    def size(self) -> int:
        return self.__size

    def is_empty(self) -> bool:
        return self.size == 0

    def contains(self, element: int) -> bool:
        return self.__index_of__(element) != ELEMENTS_NOT_FOUND

    def add(self, element: int):
        self.insert(index=self.__size, element=element)

    def get(self, index: int) -> int:
        self.__range_check__(index)
        return self.__elements[index]

    '''
    用新的element替换角标为index的元素
    '''
    def set(self, index: int, element: int) -> int:
        self.__range_check__(index)
        self.__elements[index] = element
        return 0

    # 插入
    def insert(self, index: int, element: int):
        self.__range_check_for_add__(index)

        self.__ensure_capacity__(self.__size + 1)

        for i in range(self.__size, index, -1):
            self.__elements[i] = self.__elements[i-1]
        self.__elements[index] = element
        self.__size += 1

    def remove(self, index: int):
        self.__range_check__(index)

        for i in range(index, self.__size - 1):
            self.__elements[i] = self.__elements[i+1]
        self.__size -= 1

    def remove_object(self, element: int):
        pass

    def clear(self):
        self.__size = 0

    def __ensure_capacity__(self, capacity: int):
        old_capacity = len(self.__elements)
        if old_capacity >= capacity:
            return
        new_capacity = old_capacity + (old_capacity >> 1)
        new_elements = [None] * new_capacity
        for i in range(self.__size):
            new_elements[i] = self.__elements[i]
        self.__elements = new_elements

        print('%d扩容成%d' % (old_capacity, new_capacity))

    def __index_of__(self, element: int) -> int:
        for (index, element) in enumerate(self.__elements):
            if element == element:
                return index
        return ELEMENTS_NOT_FOUND

    '''
    检查下标值
    '''
    def __range_check__(self, index: int):
        if index < 0 or index >= self.__size:
            self.__out_of_bounds__()

    '''
    添加元素时, 检查下标值
    可以等于size 等于size时表示加到最后
    '''
    def __range_check_for_add__(self, index: int):
        if index < 0 or index > self.__size:
            self.__out_of_bounds__()

    def __out_of_bounds__(self):
        raise RuntimeError('out of bounds')

    def __str__(self):
        return str(self.__elements)


arr = ArrayList()

arr.insert(0, 11)
arr.add(22)
arr.add(33)
arr.add(44)
arr.add(55)

for i in range(30):
    arr.add(i)

# assert arr.get(0) == 11
print(arr)
print('-----------')

arr.insert(1, 66)
print(arr)
arr.remove(2)
print(arr)
arr.add(77)
print(arr)

print('-----------')

arr.clear()

print(arr)
arr.add(101)
arr.add(102)
print(arr)
