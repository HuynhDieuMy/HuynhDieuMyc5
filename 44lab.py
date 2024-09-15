# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:28:38 2024

@author: hdm 
"""

n = int(input("Nhập vào số nguyên n để tính(1/2 + 3/4 + ... + (2n+1)/(2n+2) "))
tinh = 0
for i in range (0, n + 1):
    tinh += ((2 * i) + 1) / ((2 * i) + 2)
print("Kết quả là: ",tinh)