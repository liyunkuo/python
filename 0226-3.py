# -*- coding: utf-8 -*-
"""
1100226
作業三

由使用者輸入數值，
透過for迴圈做1~輸入值的加總，
最後印出總和。
"""

num = int(input("請輸入大於1的數字："))
total = 0

for i in range(1,num + 1) :
    total += i

print("數字 1 ~",num,"的加總為：",total)
    
print("程式執行完畢")