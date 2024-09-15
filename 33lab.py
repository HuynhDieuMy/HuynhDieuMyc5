# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:26:05 2024

@author: hdm 
"""

n = int(input("Nhập vào số n: "))
for i in range(1, n + 1):
    if i * i == n:
        print(n,"Đây là số chính phương")
        break
else:
    print(n,"Đây không phải là số chính phương")