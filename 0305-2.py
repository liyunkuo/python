# -*- coding: utf-8 -*-
"""
1100305
作業二

1~49之間亂數取6個不重複數字，並印出。
"""

import random

number = list()

while len(number) < 6 :
    num = random.randint(1,49)
    if number.count(num) == 0 :    # 判別是否有重複數字
        number.append(num)
        
print("隨機取六數結果為：",number)
