# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:54:00 2024

@author: hdm
"""
sotrendong = 0  
for i in range(1000, 2000):
    print(i, end=" ")  
    sotrendong += 1
    if sotrendong == 5:
        print()
        sotrendong = 0
