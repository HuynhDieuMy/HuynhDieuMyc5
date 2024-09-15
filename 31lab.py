# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 01:24:02 2024

@author: hdm
"""
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = int(input("Nhập số c: "))
loai = [(a == b == c, "Tam giác đều."),
    (a == b or b == c or a == c, "Tam giác cân."),
    (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2, "Tam giác vuông."),
    (a + b > c and a + c > b and b + c > a, "Tam giác thường.")]
for dk, tamgiac in loai:
    if dk:
        print(tamgiac)
        break
else:
    print("Hông phải tam giác")
