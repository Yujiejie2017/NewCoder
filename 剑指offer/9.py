'''
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        #对于第n个台阶来说，只能从n-1或n-2，。。。1,0的台阶跳上来，所以
        #F(n) = F(n-1) + F(n-2) +... + F(0)
        listn = [1,1,2]
        if number < 3:
            pass
        else:
            while(1):
                listn.append(sum(listn))
                if number == len(listn) - 1:
                    break
        return listn[number]