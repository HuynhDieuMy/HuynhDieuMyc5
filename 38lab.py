# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:27:37 2024

@author: L13
"""

n = int(input("Nhập vào số lẻ dương n để tính(1 * 2 * 3 * ... * n) "))
tinh = 1
for i in range (1, n + 1):
    tinh = tinh * i
print("Kết quả là: ",tinh)