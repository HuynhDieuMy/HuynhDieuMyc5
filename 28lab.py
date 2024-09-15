# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:14:43 2024

@author: hdm 
"""
while True:
    so = input("Nhập số nguyên dương: ")
    if so.isdigit() and int(so) > 0:
        so = int(so)
        break
    else:
        print("Nhập sai gòy, nhập lại đii.")
        continue
print(f"Các ước của {so} là:")
for i in range(1,so):
    if so % i == 0:
       print(i, end='\t')
