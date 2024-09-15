# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:28:18 2024

@author: hdm 
"""

n = int(input("Nhập vào số nguyên n để tính(1 + 1/3 + 1/5 + ... + 1/(2n+1)) "))
tinh = 0
for i in range (0, n + 1):
    tinh += 1 / ((2 * i) + 1)
print("Kết quả là: ",tinh)