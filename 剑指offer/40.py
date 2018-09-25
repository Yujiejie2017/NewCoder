'''
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。
请写程序找出这两个只出现一次的数字。
'''


# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        array2 = list(set(array))
        aan = [0] * len(array2)
        for a in array:
            for j in range(len(array2)):
                if array2[j] == a:
                    aan[j] += 1

        A = []
        for i in range(len(aan)):
            if aan[i] == 1:
                A.append(array2[i])
        return A