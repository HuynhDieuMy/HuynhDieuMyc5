# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:42:16 2024

@author: hdm 
"""
import random
sotran = int(input("Nhập vào số lần muốn khiêu : "))
tran = 0
hoa = 0
diemnguoi = 0
diemmay = 0
while tran < sotran:
    nguoi = input("Bạn chọn gì nào (kéo, búa, bao): ")
    may = random.choice(['kéo', 'búa', 'bao'])
    tran = tran + 1
    
    print("\tTrận: ", tran)
    print("\tNgười chọn: ", nguoi)
    print("\tMáy chọn: ", may)
    if nguoi == may:
        hoa = hoa + 1
        print("\t Hòa nha.")
    elif (nguoi == 'kéo' and may == 'bao') or\
         (nguoi == 'búa' and may == 'kéo') or\
         (nguoi == 'bao' and may == 'búa'):
        diemnguoi = diemnguoi + 1
        print("\tYou winnn!")
    else:
        diemmay = diemmay + 1
        print("\tYou lose :<")
    print("\tĐiểm người: ", diemnguoi, "Điểm máy: ", diemmay, "Hòa: ", hoa)
    continue
