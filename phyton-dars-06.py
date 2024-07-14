# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 17:35:04 2023

@author: hp
"""

f = 20
h = 5.5
tempq = 36.6
print(type(h))
aholi_soni = 7_594_376_567
print("Aholi soni:",aholi_soni, "ta");

x, y, z = 10, 5.5, -52
print(x, y,z)

c = f*h
print(c)


ism = "Jobir"
yosh = 36 # bu int bo'lgani uchun xato ko'rsatadi, matn ko'rinishiga o'tkazish uchun str() ishlatiladi
xabar = ism + ' ' + str(yosh) + ' yoshda'
print(xabar)

t_yil = int(input("Tug'ilgan yilingizni kiriting...")) # int butun (5217) songa o'tkazadi 
yosh = 2023 - t_yil
print("Siz ", yosh, "yoshda ekansiz")



# int lyuboy(25) sonni butun(23) son ko'rinishiga keltiradi
# float lyuboy(12) sonni (36.5) ga o'tqazadi
# str lyuboy(12) sonni matn("10") ko'rinishiga o'tkazadi

a = int("12")      # 10
b = float("23")    # 10.0
temp = str(2.5)    # 2.5
print(a,b,temp)
