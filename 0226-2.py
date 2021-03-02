# -*- coding: utf-8 -*-
"""
1100226
作業二

使用for迴圈讓程式執行結果為
123456789
12345678
1234567
123456
12345
1234
123
12
1
"""

times = 10

for i in range(1,times) :
    for j in range(1,times) :
        print(j,end = ' ')
    print()                 # 換行
    times -= 1
    
print("程式執行完畢")