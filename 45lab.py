# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:28:43 2024

@author: hdm 
"""

print("Tính x + (x^2)/(1+2) + (x^3)/(1+2+3) ... + (x^n)/(1+2+3+...+n)")
x = float(input("Nhập vào số x: "))
n = int(input("Nhập vào số nguyên n: "))
tinh = 0
ntang = 0
for i in range (1, n + 1):
    ntang += i
    tinh += (x ** i) / ntang
print("Kết quả là: ",tinh)