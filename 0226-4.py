# -*- coding: utf-8 -*-
"""
1100226
作業四

使用for迴圈，列出菱形圖形：
   *
  ***
 *****
*******
 *****
  ***
   *
"""

for i in range(1,5) :
    for j in range(1,5) :       # 左上角
        if (i+j) < 5 :
            print(" ",end = '')
        else :
            print("*",end = '')
    for k in range(1,4) :       # 右上角
        if i >= 2 and j >= 4 and (i+k) > 4 :
            print("*",end = '')
    print()

times = 2

for i in range(1,5) :
    for j in range(1,5) :       # 左下角
        if (i+j) > times :
            print("*",end = '')
        else :
            print(" ",end = '')
    for k in range(1,3) :       # 右下角
        if i < 3 and (i+k) >= times :
            print("*",end = '')
    print()
    times += 2

print("程式執行完畢")