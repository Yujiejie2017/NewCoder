'''
题目描述
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,
并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。
LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何，
如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。
'''
# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers)== 0:
            return False
        else:
            list1 = sorted(numbers)
            n_0 = 0
            for i in range(len(list1)):
                if list1[i] == 0:
                    n_0 += 1
                else:
                    break
            list2 = list1[n_0:]
            totall = 0
            for i in range(1,len(list2)):
                t = list2[i] - list2[i-1]
                if t >0:
                    totall += t - 1
                elif t <= 0:
                    return False
                    break
            if n_0 >= totall:
                return True
            else:
                return False