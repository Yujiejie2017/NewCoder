'''
题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        array1 = []
        array2 = []
        for i in range(len(array)):
            if array[i] % 2 == 1:
                array1.append(array[i])
            else:
                array2.append(array[i])
        for i in range(len(array2)):
            array1.append(array2[i])
        return array1