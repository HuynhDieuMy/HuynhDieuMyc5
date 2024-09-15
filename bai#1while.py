# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:52:01 2024

@author: Huynh Dieu My 
"""
x = float(input("Nhập vào số x: "))
while x < -99 or x > 99:
    x = float(input("Nhập lại x: "))
print("Giá trị đã nhập ", x)