# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:28:23 2024

@author: hdm 
"""

n = int(input("Nhập vào số nguyên n để tính(1/(1*2) + 1/(2*3) + ... + 1/(n*(n+1)) "))
tinh = 0
for i in range (1, n + 1):
    tinh += 1 / (i * (i +1))
print("Kết quả là: ",tinh)