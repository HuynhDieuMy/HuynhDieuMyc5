# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:05:18 2024

@author: hdm 
"""
import random
n = int(input("Nhập một số nguyên n: "))
songaunhien = [random.random() for i in range(n)]
tb = sum(songaunhien) / n
nhonhat = min(songaunhien)
lonnhat = max(songaunhien)
print(f"Các số ngẫu nhiên: {songaunhien}")
print(f"Trung bình: {tb}")
print(f"Giá trị nhỏ nhất: {nhonhat}")
print(f"Giá trị lớn nhất: {lonnhat}")