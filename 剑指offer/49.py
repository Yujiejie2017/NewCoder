'''
题目描述
将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述:
输入一个字符串,包括数字字母符号,可以为空
输出描述:
如果是合法的数值表达则返回该数字，否则返回0

示例1
输入

+2147483647
    1a33
输出

2147483647
    0

'''
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        numlist=['0','1','2','3','4','5','6','7','8','9']
        sum=0
        label=1#正负数标记

        if s=='':
            return 0

        if s[0]=="+":
            label = 1
            s = s[1:]
        elif s[0]=="-":
            label = -1
            s = s[1:]
        else:
            pass
        for string in s:
            if string in numlist:
                sum=sum*10+numlist.index(string)
            elif string not in numlist:#非合法字符
                sum=0
                break#跳出循环

        return sum * label