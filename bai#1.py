# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:44:02 2024

@author: Huynh Dieu 
"""

n = int(input("Nhập vào số nguyên cần tính giai thừa: "))
S = 1
for i in range(1, n+1):
    S = S*i
print("Giai thừa của",n,"là: ", S)