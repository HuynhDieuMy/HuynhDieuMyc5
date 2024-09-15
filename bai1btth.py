# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:01:04 2024

@author: hdm 
"""

chuoi = input("Nhập chuỗi: ")
len(chuoi)
kytudacbiet =  '!@$%^&*()-=+./'
dayktdb = [i for i in chuoi if i in kytudacbiet]
print(dayktdb)
print(len(dayktdb))

chuthuong = [e for e in chuoi if e.islower()]
print(chuthuong)
print(len(chuthuong))

so = [u for u in chuoi if u.isdigit()]
print(so)
print(len(so))

chuhoa = [a for a in chuoi if a.isupper()]
print(chuhoa)
print(len(chuhoa))