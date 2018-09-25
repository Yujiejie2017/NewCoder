
'''
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        '''
        def uglynumber(number):
            while (number % 2 == 0):
                number /= 2
            while (number % 3 == 0):
                number /= 3
            while (number % 5 == 0):
                number /= 5
            return number == 1
        N = 0
        i = 1
        while(1):
            if uglynumber(i):
                N += 1
            if index == N:
                return i
                break
            i += 1
            '''
        res=[2**i*3**j*5**k  for i in range(50)  for j in range(30)   for k in range(20)]
        res.sort()
        return res[index-1] if index else 0