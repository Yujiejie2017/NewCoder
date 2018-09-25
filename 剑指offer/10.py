
'''
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        #对于n，只能从n-1或n-2覆盖而来
        #F(n) = F(n-1) + F(n-2）
        #F(0) = 0
        #F(1) = 1
        #F(2) = 2
        listn = [0,1,2]
        if number < 3:
            pass
        else:
            while(1):
                listn.append(listn[-1] + listn[-2])
                if number == len(listn) - 1:
                    break
        return listn[number]