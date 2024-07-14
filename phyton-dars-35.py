# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:27:23 2023

@author: hp
"""

#                              35 - dars try,except

# yosh = input("yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
#     print(f"Siz {2023-yosh} yilda tug'ilgansiz")
# except:
#     print("Siz butun son kiritmadingiz.")
# print'(*****************************************************************************')

# yosh = input("yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except:
#     print("Siz butun son kiritmadingiz.")
# else:
#     print(f"Siz {2023-yosh} yilda tug'ilgansiz")
# print'(*****************************************************************************')

# yosh = input("yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)
# except ValueError:
#     print("Siz butun son kiritmadingiz.")
# else:
#     print(f"Siz {2023-yosh} yilda tug'ilgansiz")
# print'(*****************************************************************************')

# ZeroDivisionError 0 ga bo'linmaydi
# x,y = 5,10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# print'(*****************************************************************************')  

# mevalar = ['olma','anor','anjir','uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yhatda {len(mevalar)} ta meva bor xolos")
# print'(*****************************************************************************')        

# user = {'username':'sariqdev',
#         'status':'admin',
#         'email':'admin@sariq.dev',
#         'phone':'998935197907'}
# key = 'tel'
# try:
#     print(f"Foydalanuvchi: {user[key]}")
# except KeyError:
#     print("Bunday kalit mavjud emas")
# print'(*****************************************************************************') 

# filename = 'data.txt' # bunday fayl mavjud emas
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotError:
#     print(f"{filename} mavjud emas")
# print'(*****************************************************************************')     
    
# import json
# files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)
#     except FileNotFoundError:
#         print(f"{filename} mavjud emas") # or pass
#     else:
#         print(talaba['ism'])
# print'(*****************************************************************************') 

# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x = 20/n
# except ValueError:
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     print(f"x={x}")
# print'(*****************************************************************************') 

while True:
    yosh = input("yoshingizni kiriting: ")
    if yosh.isdigit(): # sonmi raqammiligini tekshirish
        yosh = int(yosh)
        break
print(f"Siz {2023-yosh} yilda tug'ilgansiz")
    








