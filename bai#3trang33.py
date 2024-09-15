# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:56:57 2024

@author: HDM 
"""
n = int(input("Nhập n: "))
dict = {i: i**i for i in range(1, n+1)}
print(dict)