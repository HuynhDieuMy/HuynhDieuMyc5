# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:27:09 2024

@author: hdm 
"""
n = int(input("Nhập vào số nguyên dương n để tính(1^2 + 2^2 + ... + n^2) "))
tinh = 0
for i in range (1, n + 1):
    tinh += i ** 2
print("Kết quả là: ",tinh)
