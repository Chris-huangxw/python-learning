#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#阶乘的实现，n的阶乘就是从1x....xn
def cheng(a):
    result = a;
    for i in range(1, a):
        result *= i
    print result

#使用递归实现阶乘
def degui(n):
    if n == 1:
        return 1
    else:
        return n*degui(n-1)

#使用二分查找
'''
使用二分查找的前提下需要对seq进行sort（）排序，才能保证准确性
assert断言，一定有seq[upper]
标准库中bisect模块可以有效实现二分查找
'''
def search(seq, num, lower, upper):
    if lower == upper:
        assert number == seq[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > seq[middle]:
            return search(seq, number, middle, upper)
        else:
            return search(seq, number, lower, middle)



if __name__ == '__main__':
     print map(str, range(10))
