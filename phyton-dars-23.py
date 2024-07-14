# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:00:12 2023

@author: hp
"""

#                                MODUL

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# def avto_kirit():
#     """Foydalanuvchiga funksiya yordamida bir nechta avtolar haqida malumot berish"""
#     avtolar = [] # salondagi avtolar uchun bo'sh ro'hat
#     while True:
#         print("\nQuyidagi ma'lumotlarni kiriting")
#         kompaniya = input("Ishlab chiqaruvchi: ")
#         model = input("Modeli: ")
#         rangi = input("Rangi: ")
#         korobka = input("Korobka: ")
#         yili = input("Ishlab chiqarilgan yili: ")
#         narhi = input("Narhi: ")
#         #  Foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
#         # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#         avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narhi))
#         javob = input("Yana avto qo'shasizmi? (yes/no): ")
#         if javob == 'no':
#             break

# def info_print(avto_info):
#     """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
#     print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()}) "
#           f"{avto_info['model'].upper()},{avto_info['korobka']} korobka, "
#           f"{avto_info['yili']}-yili,{avto_info['narh']}$")


# import math
# x = 400
# print(math.sqrt(x))
# print(math.pow(5,3))
# print(math.pi)
# print(math.log10(100))
# print(math.log2(8))

import random as r   # from random import choice, randint
# # randint() 
# son = r.randint(0,100)
# print(son)

# # choice()
# ismlar = ['olim','anvar','hasan','husan']
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))  # ismdagi tanlangan ismdan tasodifiy bitta harfni chiqarib beradi.

# x = list(range(0,50,5))
# print(x)
# print(r.choice(x))


# # shuffle() - listning o'rnini aralashtirib tashlaydi.
# x = list(range(11))
# print(x)
# r.shuffle(x)
# print(x)



#                                    24 - dars

# lambda - bu ham funksiya def ga o'xshagan (nomsiz funksiya)

# import math
# def nom(argument):
#   return ifoda

# lambda argument : ifoda

# uzulik = lambda pi, r : 2*pi*r
# print(uzulik(math.pi,10))

# kvadrat = lambda x, y : x**y
# print(kvadrat(3,9))

# def daraja(n):
#     return lambda x : x**n
# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3 ning kubi {kub(3)} ga, 4 ning kvadrati {kvadrat(4)}ga teng.")

# map - bu

# from math import sqrt

# sonlar = list(range(11))
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)

# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x
# print(list(map(daraja2,sonlar)))

# kvadratlar = list(map(lambda x:x*x , sonlar))
# print(kvadratlar)

# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x,y : x+y, a, b))
# print(a_plus_b)

 
import random as r

# sample() - tasodifiy sonlar 
sonlar = r.sample(range(100),10)
# print(sonlar)
def juftmi(x):
    """x juft bo'lsa True,aks holda False qaytaruvchi funksiya"""
    return x%2==0

# filter() - saralash
# juft_sonlar = list(filter(juftmi,sonlar))
# print(juft_sonlar)
# burni o'rniga onsorrog'i

juft_sonlar = list(filter(lambda x: x%2 ==0,sonlar))
# print(juft_sonlar)

# .startswith() - matnlar bilan ishlash, harf bilan boshlanadimi yo'q
mevalar = ['olma', 'anor','anjir','shaftoli',"o'rik",'tarvuz',"qovun",'banan']
harf = 'b'
mevalar_b = list(filter(lambda meva:meva.startswith(harf),mevalar))
print(mevalar_b)

mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))

meva = list(filter(lambda meva:meva.startswith('s') and meva.endswith('r'),mevalar))
print(meva)










