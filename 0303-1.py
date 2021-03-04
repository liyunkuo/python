# -*- coding: utf-8 -*-
"""
1100303
作業一

請將猜數提示改為詳細區間的敘述
"""

import random

count = 1
ans = random.randint(1,100)
minnum = 1
maxnum = 100

guess = int(input("請輸入1-100之間的整數："))
# print("您猜的是第%d次"%count)

while ans != guess :
    if ans > guess :
        minnum = guess + 1
        guess = int(input("請輸入%d-%d之間的整數："%(minnum,maxnum)))
        count += 1
        # print("您猜的是第%d次"%count)
    if ans < guess :
        maxnum = guess - 1
        guess = int(input("請輸入%d-%d之間的整數："%(minnum,maxnum)))
        count += 1
        # print("您猜的是第%d次"%count)

print("猜對了，猜對的數字為：%d，共猜：%d次"%(ans,count))
