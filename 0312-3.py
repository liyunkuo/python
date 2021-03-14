# -*- coding: utf-8 -*-
"""
1100312
作業三

一個整數：它加上１００後是一個完全平方數，
再加上１６８又是一個完成平方數，請問它是多少？
"""

import math


for num in range(1,1001) :
    n = math.sqrt(num + 100)
    m = math.sqrt(num + 268)
    if n == int(n) and m == int(m) :
        print(num)
