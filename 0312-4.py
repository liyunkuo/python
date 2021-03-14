# -*- coding: utf-8 -*-
"""
1100312
作業四

輸入三個整數ｘ，ｙ，ｚ
請把這三個數由小到大輸出
"""

number = [0,0,0]

print('請輸入三個整數：')

for i in range(0,3) :
    print('第{}個整數：'.format(i+1),end = '')
    number[i] = int(input())
    
numbers = sorted(number)
    
print('這三個整數排序為：',numbers)
