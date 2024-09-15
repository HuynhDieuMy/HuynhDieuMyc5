# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:11:50 2024

@author: hdm 
"""
email = input("Nhập email: ")
if email.count('@') !=1:
    print("Vui lòng nhập lại email chính xác!")
else:
    truoc, sau = email.split('@')
    if len(truoc) < 6:
        print("Email sai: Phần trước @ phải trên 6 kí tự!")
    else:
        emailtrang = True
        emailkitu = True
        for i in truoc:
            if i == ' ':
                emailtrang = False
            elif not i.isalnum():
                emailkitu = False
        if emailtrang == False:
            print("Email sai: Phần trước @ không được chứa khoảng trắng")
        elif emailkitu == False:
            print("Email sai: Phần trước @ không được chứa kí tự đặc biệt")