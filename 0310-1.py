# -*- coding: utf-8 -*-
"""
1100310
作業一

2/1,3/2,5/3,8/5,13/8,21/13,...,求前20項之和。
"""

denonum = 1
nonum = 2
num = 0

for i in range(1,21):
    num += nonum / denonum
    denonum,nonum = nonum,denonum + nonum
    
print('總和為：',num)