'''
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''


# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        '''
        n = number
        def C(m,n):
            num = 0
            uper = 1
            while(1):
                uper *= n
                n -= 1
                num += 1
                if num == m:
                    break
            downer = 1
            while(1):
                downer *= m
                m -= 1
                if m == 0:
                    break
            return uper/downer
        def A(m,n):
            A = 1
            while(1):
                A *= n
                n -= 1
                m -=1
                if m == 0:
                    break
            return A

        totall = 0


        for i in range(number+1):
            if i * 1 + (number - i) * 2 == number:
                totall += A(i, number) * C(number - i, number) * A(2,2)
                #totall += A(number, number)/(A(i, i) * A(number - i, number - i))
            else:
                pass
        return totall
        '''
        '''
        对于第n个台阶来说，只能从n-1或者n-2的台阶跳上来，所以
        F(n) = F(n-1) + F(n-2)
        斐波拉契数序列，初始条件
        n=1:只能一种方法
        n=2:两种
        '''

        '''
        listn = [0,1,2]
        if number <3:
            return listn[number]
        else:
            while(1):
                listn.append(listn[-1] + listn[-2])
                if number == len(listn) - 1:
                    break
            return listn[number]
        '''
        listn = [0, 1, 2]
        if number < 3:
            pass
        else:
            while (1):
                listn.append(listn[-1] + listn[-2])
                if number == len(listn) - 1:
                    break
        return listn[number]

        '''
        n_list = [0,1,2]
        if number < len(n_list):
            return n_list[number]
        else:
            while(1):
                n_list.append(n_list[-1]+n_list[-2])
                if number  == len(n_list) - 1:
                    break
            return n_list[number]
            '''