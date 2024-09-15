# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:28:31 2024

@author: hdm 
"""

n = int(input("Nhập vào số nguyên n để tính(1/2 + 2/3 + ... + n/(n+1) "))
tinh = 0
for i in range (1, n + 1):
    tinh += i / (i + 1)
print("Kết quả là: ",tinh)