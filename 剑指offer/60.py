'''
题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，
每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

'''


# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        def number(N):
            N = str(N)
            nn = 0
            for i in range(len(N)):
                nn += int(N[i])
            return nn

        num = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if number(i) + number(j) <= threshold:
                    num += 1
        return num

'''
您的代码已保存
答案错误:您提交的程序没有通过所有的测试用例
case通过率为0.00%

测试用例:
5,10,10

对应输出应该为:

21

你的输出为:

19
'''