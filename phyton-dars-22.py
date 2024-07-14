# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 17:56:09 2023

@author: hp 
"""

                                                # 22 dars

                         # *args va **kwargs
# *args

def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi
print(summa(1,2))
print(summa(1,2,5,4,2))
print(summa(1,2,3,4,5))
a = summa(123,435,3745,6234,45436)
print(a)
print('*******************************************')

def summasi(*sonlar):
    """Oson varianti"""
    return sum(sonlar)
b = summasi(124,4536,67,657,34,243,567,58434,536470)
print(b)

# 2
def summa(x, y, *sonlar,t):
    """Oson varianti"""
    return x+y+sum(sonlar)
print(summa(1,2,7,3, t=1))

# 3
def avto_info(kompaniya, model,turi,**malumotlar):
    """Avto haqida ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya'] = kompaniya,
    malumotlar['model'] = model,
    malumotlar['Markasi'] = turi
    return malumotlar
avto1 = avto_info("GM", "Malibu",'Ferra', rang = "Qora", yili = 2018)
avto2 = avto_info("GM","Gentra",'Lambo',rang = "Oq", yili = 2018, narxi = 15000)
avtolar = [avto1,avto2]
print(avtolar)













