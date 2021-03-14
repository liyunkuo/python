# -*- coding: utf-8 -*-
"""
1100312
作業六

印出　９ｘ９　法表
"""

for i in range(2,10) :
    for j in range(2,10) :
        num = i * j
        print("{:2d}x{:2d}={:2d}".format(j,i,num),end = ' ')
    print()
