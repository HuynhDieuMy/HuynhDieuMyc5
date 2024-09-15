# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:34:02 2024

@author: Huynh Dieu My 
"""

import random
soluong = 0 
for i in range(random.randrange(1,83)):
    so = random.uniform(18,99)
    binhphuong = so **2
    soluong = i + 1
    print(so, "^2 =", binhphuong, end=', \t' )
print("\nCó tâtr cả: ", soluong, "Số bình phương")
    
    