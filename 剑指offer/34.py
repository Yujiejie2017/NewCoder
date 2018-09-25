'''
题目描述
在一个字符串(0<=字符串长度<=10000，
全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
'''
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s)==0:
            return -1
        ss = ""
        for i in range(len(s)):
            if s[i] not in ss:
                ss += s[i]
        ssn = [0]*len(ss)
        for i in range(len(s)):
            for j in range(len(ss)):
                if s[i] == ss[j]:
                    ssn[j] += 1

        AAn = 0
        for k in range(len(ssn)):
            if ssn[k] == 1:
                AAA = ss[k]
                break
        for i in range(len(s)):
            if s[i] == AAA:
                return i
                break