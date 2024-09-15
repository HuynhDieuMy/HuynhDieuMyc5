# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:13:06 2024

@author: L13
"""

danhsach = []
for i in range(2018, 2829):
    if i % 2 ==0 and i % 5 ==0 :
        danhsach.append(i)
print(danhsach)