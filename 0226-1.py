# -*- coding: utf-8 -*-
"""
1100226
作業一

程式執行結果為
1
12
123
1234
"""


for i in range(1,5) :
    for a in range(1,i + 1) :
        print(a,end = ' ')
    print()                 # 換行  
print("程式執行完畢")