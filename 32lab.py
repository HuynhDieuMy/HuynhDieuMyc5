# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:24:19 2024

@author: hdm 
"""

sokm = int(input("Nhập số km TAXI đi được: "))
tien = 0
for km in range(1, sokm + 1):
    if km == 1:
        tien += 15000
    elif 2 <= km <= 5:
        tien += 13500
    elif km >= 6:
        tien += 11000
if sokm > 120:
    tien = tien * 0.9
print(f"Tiền cước TAXI phải trả là: {tien} đồng")