# -*- coding: utf-8 -*-
"""
1100305
作業一
氣泡排序法

鄰近兩數做比較，大的數值往右移。
"""

number = list()

while len(number) <= 5 :
    num = int(input("請輸入數字："))
    number.append(num)

print("串列內容：",number)
print("氣泡排序法：",end = '')

for k in range(6) :                   # 最外圍(總共要比六次)
    for i in range(5) :                   # 一次鄰近兩數做比較
        for j in range(i + 1,i + 2) :
            if number[i] > number[j] :
                temp = number[j]
                number[j] = number[i]
                number[i] = temp

print(number)