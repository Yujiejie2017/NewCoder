'''
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，
使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
'''

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        AA = []
        for i in range(len(array)-1):
            for j in range(i+1,len(array)):
                if array[i] + array[j] == tsum:
                    AA.append([array[i],array[j],array[i] * array[j]])
                    break
        if len(AA) == 0:
            return AA
        else:
            AA = sorted(AA, key = lambda aa:aa[2])
            return AA[0][:2]