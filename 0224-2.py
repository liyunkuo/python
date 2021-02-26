# -*- coding: utf-8 -*-
"""
1100224

作業二

輸入迴圈(for)的次數，計算數值中為偶數的加總，最後印出加總的值。
"""

number = int(input("請輸入迴圈的次數："))
count = 0

for num in range(1,number + 1) :
    if num % 2 == 0 :
        print(num,end = ' ')
        count += num
        
print("數字為偶數")
print("偶數的加總為：",count)

print("程式執行完畢")
