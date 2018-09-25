'''
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
则打印出这三个数字能排成的最小数字为321323。
'''

# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        def Permutation(ss):
            # write code here
            if len(ss) == 0:
                return []
            if len(ss) == 1:
                return [ss]
            res = set()
            for i in range(len(ss)):
                for j in Permutation(ss[:i] + ss[i + 1:]):
                    res.add(ss[i] + j)
            return sorted(list(res))
        if len(numbers) == 0:
            return ""
        else:
            A = numbers
            for i in range(len(A)):
                A[i] = str(A[i])

            B = [str(i) for i in range(len(A))]
            bb = ""
            for i in range(len(B)):
                bb += B[i]
            SSS = Permutation(bb)
            minN = 999999999999999999999999999999999999
            for i in range(len(SSS)):
                sss = ""
                for j in range(len(SSS[i])):
                    sss += A[int(SSS[i][j])]
                minN = min(minN, int(sss))

            return minN