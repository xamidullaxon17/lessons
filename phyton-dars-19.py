# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 16:59:07 2023

@author: hp
"""

                                    # 19 - dars. Funksiya

# 1
def ism_yosh(ism,yosh):
    """Bu foydalanuvchining ismini va familyasini aniqlab beradi"""
    print(f"Foydalanuvchining ismi {ism}")
    print(f"Foydanaluvchining yoshi {yosh}")
    
ism_yosh('Alisher',23)

# 2
def son_kv(son):
    """Sonning kvadratini aniqlovchi funksiya"""
    print(f"{son} ning kvadrati {son**2} ga teng")
son_kv(5)

# 3
def son_jt(son1):
    """Foydalanuvchidan son olib uning juft yoki toqligini aniqlovchi funksiya"""
    if son1 % 2:
        print(f"{son1} toq son")
    else:
        print(f'{son1} just son')
son_jt(1)

# 4
def son2(son,son1):
    """sonning kattasini aniqlovchi dastur"""
    if son<son1:
        print(f'{son1} katta')
    elif son>son1:
        print(f'{son} katta')
    else:
        print("sonlar teng")
son2(56,34)

# 5
def son2(s1,s2):
    """sonnnig kvadratinin chiqaruvchi funksiya"""
    a = s1**s2
    print(a)
son2(2,4)

# 6
def son3(s2,s3=2):
    """Bu yerda y standart son"""
    b = s2**s3
    print(b)
son3(3)
print("******************")
# 7
def son10(son1):
    """Sonning 2dan 10gacha qoldiqsiz bo'linishi"""
    for n in range(1,11):
         if son1 % n == 0:
             print(n)
son10(30)

# 7 boshqacharog'i uy ishi javobiniki

def son10(son1):
    """Sonning 2dan 10gacha qoldiqsiz bo'linishi"""
    for n in range(2,11):
         if not son1 % n: 
             print(f"{son1} {n} ga qoldiqsiz bo'linadi")
son10(30)





































                                    