'''
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，
请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        #F(1)=1，F(2)=1, F(n)=F(n-1)+F(n-2)（n>=3，n∈N*）
        '''
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            return Fibonacci(seln-1) + Fibonacci(self, n-2)
        '''
        n_list = [0,1,1]
        if n < len(n_list):
            return n_list[n]
        else:
            while(1):
                n_list.append(n_list[-1]+n_list[-2])
                if n  == len(n_list) - 1:
                    break
            return n_list[n]