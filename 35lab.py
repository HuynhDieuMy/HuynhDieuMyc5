# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:26:57 2024

@author: hdm 
"""

n = int(input("Nhập vào số n để tính(1 + 2 + 3 + ... + n) "))
tinh = 0
for i in range (1, n + 1):
    tinh += i
print("Kết quả: ",tinh)