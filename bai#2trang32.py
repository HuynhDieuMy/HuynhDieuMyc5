# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:19:55 2024

@author: HDM 
"""

danhsach = []
for i in range(2020, 3839):
    if i % 9 == 0 and i % 2 == 0:
        danhsach.append(i)
print(danhsach)
print("\t".join(map(str, danhsach)))