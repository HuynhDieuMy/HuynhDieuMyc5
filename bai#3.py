# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:05:20 2024

@author: Huynh Dieu My 
"""
import random
soluong = 0
for i in range(random.randrange(1,12)):
    phantu = random.randrange(20,30)
    print(phantu, end=' ')
    soluong = i + 1
print("Số lượng phần tử đã in là: ", soluong)
    
