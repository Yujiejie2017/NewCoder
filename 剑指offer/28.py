'''
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        B = sorted(list(set(numbers)))
        C = [0] * len(B)
        for i in range(len(numbers)):
            for j in range(len(B)):
                if numbers[i] == B[j]:
                    C[j] += 1
        if max(C) <= len(numbers)/2:
            number = 0
        elif max(C) > len(numbers)/2:
            n = C.index(max(C))
            number = B[n]
        return number