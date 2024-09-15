# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:26:43 2024

@author: hdm 
"""

n = int(input("Nhập vào số n: "))
for i in range(2, n):
    if n % i == 0:
        print(n,"Không phải là số nguyên tố!")
        break
else:
    print(n,"Đây là số nguyên tố")