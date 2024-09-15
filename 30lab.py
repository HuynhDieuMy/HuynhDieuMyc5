# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:23:26 2024

@author: hdm 
"""
thang = int(input("Nhập vào tháng : "))
nam = int(input("Nhập vào năm: "))
ngaytrongthang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   
if (nam % 100 != 0 and nam % 4 == 0 ) or (nam % 400 == 0):
    ngaytrongthang[1] = 29
for i in range(1, 13):
    if thang == i:
        print(f"Tháng {thang} năm {nam} có {ngaytrongthang[i-1]} ngày.")
        break
