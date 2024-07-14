# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:21:17 2023

@author: hp
"""

def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi}
    return avto

def avto_kirit():
    """Foydalanuvchiga funksiya yordamida bir nechta avtolar haqida malumot berish"""
    avtolar = [] # salondagi avtolar uchun bo'sh ro'hat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting")
        kompaniya = input("Ishlab chiqaruvchi: ")
        model = input("Modeli: ")
        rangi = input("Rangi: ")
        korobka = input("Korobka: ")
        yili = input("Ishlab chiqarilgan yili: ")
        narhi = input("Narhi: ")
        #  Foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
        # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
        avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narhi))
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob == 'no':
            break

def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()}, {avto_info['kompaniya'].upper()}, "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yili, {avto_info['narh']}$.")
    
    
    
    