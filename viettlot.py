# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 00:11:10 2024

@author: hdm 
"""
import random
sove = int(input("Bạn muốn mua bao nhiêu vé: "))
tienve = 0
dsve = []
for _ in range(1, sove + 1):
    tienve += 10000
    ve = []
    while len(ve) < 6:
        so = str(random.randint(1, 45))
        if so not in ve:
            ve += [so]
    dsve += [ve]
n = 1
for i in dsve:
    print(f"Vé thứ {n}: {'-'.join(i)}")
    n += 1
print(f"Tổng tiền mua vé số là: {tienve:,} đ")

vetrungthuong = []
while len(vetrungthuong) < 6:
    sotrungthuong = str(random.randint(1, 45))
    if sotrungthuong not in vetrungthuong:
        vetrungthuong += [sotrungthuong]
print("\nVé số trúng thưởng:",'-'.join(vetrungthuong))

giaiba = 0
giaihai = 0
giainhat = 0
giaidacbiet = 0
tienthuong = 0
for a in dsve:
    
    sotrungthuong = 0
    for u in range(6):
        if a[u] == vetrungthuong[u]:
            sotrungthuong = u + 1
    
    if sotrungthuong == 3:
        tienthuong += 30000
        giaiba += 1
    elif sotrungthuong == 4:
        tienthuong += 300000
        giaihai += 1
    elif sotrungthuong == 5:
        tienthuong += 10000000
        giainhat += 1
    elif sotrungthuong == 6:
        tienthuong += 10000000000
        giaidacbiet += 1
print("Bạn trúng: ", giaiba, "giải ba", giaihai, "giải hai", giainhat, "giải nhất", giaidacbiet, "giải đặc biệt")
print(f"Tổng số tiền trúng thưởng bạn nhận được: {tienthuong:,} đ")
