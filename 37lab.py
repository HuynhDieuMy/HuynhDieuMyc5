# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:27:24 2024

@author: hdm 
"""

n = int(input("Nhập vào số chẵn dương n để tính(2 + 4 + 6 + ... + n) "))
tinh = 0
for i in range (2, n + 1, 2):
    tinh += i
print("Kết quả là: ",tinh)