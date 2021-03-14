# -*- coding: utf-8 -*-
"""
1100312
作業五

將一個列表的數據複製到另一個列表。(不可以相互影響)
"""

import copy

a = [1,2,3,4]

b = copy.copy(a)

a[0] = 100

print(a)
print(b)