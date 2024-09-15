# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 23:51:14 2024

@author: hdm
"""
import random
nguoichoi = random.randint(8, 20)
print("Số lượng người tham gia: ", nguoichoi)
dschoi  = [f"Người chơi {i}" for i in range(1,nguoichoi +1)]
sotran = int(input("Nhập vào số trận muốn khiêu chiến: "))
hoa = 0
diemnguoichoi = [0] * nguoichoi
for tran in range(1, sotran + 1):
    print("Trận thứ: ", tran)
    nguoichon = [random.choice(['kéo', 'búa', 'bao']) for _ in range(nguoichoi)]
    for i in range(0,nguoichoi):
        print(f"{dschoi[i]} ra {nguoichon[i]}")
    tongkeo = nguoichon.count('kéo')
    tongbua = nguoichon.count('búa')
    tongbao = nguoichon.count('bao')
    if (tongkeo > 0 and tongbua > 0 and tongbao > 0) or\
       (tongkeo > 0 and tongbua == 0 and tongbao == 0) or\
       (tongkeo == 0 and tongbua > 0 and tongbao == 0) or\
       (tongkeo == 0 and tongbua == 0 and tongbao > 0):
        hoa = hoa + 1
        print("\tHòa gòy nha!")
    elif tongkeo > 0 and tongbua == 0:
        for i in range(nguoichoi):
            if nguoichon[i] == 'kéo':
                diemnguoichoi[i] = i + 1
        print("\tKéo thắng")
    elif tongbua > 0 and tongbao == 0:
        for i in range(nguoichoi):
            if nguoichon[i] == 'búa':
                diemnguoichoi[i] = i + 1
        print("\tBúa thắng")
    elif tongbao > 0 and tongkeo == 0:
        for i in range(nguoichoi):
            if nguoichon[i] == 'bao':
                diemnguoichoi[i] = i + 1
        print("\tBao thắng")
print("Kết quả cuối cùng là:")
for i in range(nguoichoi):
    print(f"{dschoi[i]} được {diemnguoichoi[i]} điểm")
print("Số hiệp hòa là: ", hoa)
