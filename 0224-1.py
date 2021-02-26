# -*- coding: utf-8 -*-
"""
1100224

作業一

輸入迴圈(for)的次數，並判斷哪些數值是偶數，哪些數值是奇數？
"""

number = int(input("請輸入迴圈的次數："))

for num in range(1,number + 1) :
    if num % 2 == 0 :
        print(num,end = ' ')
print()
        
print("數字為偶數")

for num in range(1,number + 1) :
    if num % 2 != 0 :
        print(num,end = ' ')
print()
        
print("數字為奇數")

print("程式執行完畢")
