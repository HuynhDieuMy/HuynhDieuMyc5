# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:49:37 2024

@author: L13
"""

IDuser = input("Nhập vào ID: ")
while True:
    if len(IDuser) < 6 or len(IDuser) > 24:
        print("ID phải từ 6 đến 24 ký tự")
        IDuser = input("\nNhập lại: ")
        continue

    IDktdb = True
    IDkhoangtrang = True
    for i in IDuser:
        if i in '!@#$%^&*()-=+':
            IDktdb = False
        if i == ' ':
            IDkhoangtrang = False
    if IDkhoangtrang == False:
        print("ID không được chứa dấu cách")  
            
    if IDktdb == False:
        print("ID không được chứa các ký tự đặc biệt") 
    if IDkhoangtrang == False or IDktdb == False:
        IDuser = input("\nVui lòng nhập lại ID của bạn: ")
        continue        
    break

Password = input("Nhập mật khẩu: ")    
while True:
    if len(Password) < 6 or len(Password) > 24:
        print("Độ dài Password từ 6 đến 24 ký tự")
        Password = input("\nNhập lại ID!")
        continue

    Passchuthuong = False
    Passso = False
    Passchuhoa = False
    Passktdb = False
    for u in Password:
        if u.islower():
            Passchuthuong = True
        if u.isdigit():
            Passso = True      
        if u.isupper():
            Passchuhoa = True    
        if u in '$#@':
            Passktdb = True
    if Passchuthuong == False:
        print("Password phải có ít nhất 1 chữ cái thường từ a-z")
    if Passso == False:
        print("Password phải có ít nhất 1 số từ 0-9")
    if Passchuhoa == False:
        print("Password phải có ít nhất 1 chữ cái in hoa từ A-Z")
    if Passktdb == False:
        print("Password phải  có ít nhất 1 kí tự đặc biệt trong [$ # @]")
    if Passchuthuong == False or Passso == False or Passchuhoa == False or Passktdb == False:
        Password = input("\nVui lòng nhập lại Password: ")
        continue        
    break      
print("\nPASSWORD ĐÃ ĐƯỢC LƯU!")   