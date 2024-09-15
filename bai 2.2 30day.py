# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:32:41 2024

@author: hdm 
"""

tongchan = 0
tongle = 0
for i in range(101):
    if i % 2 == 0:
        tongchan += i
    else:
        tongle += i
print("Tổng các số chẵn là:", tongchan)
print("Tổng các số lẻ là:", tongle)