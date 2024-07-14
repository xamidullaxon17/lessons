# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 16:37:16 2023

@author: hp
"""

#avtolar = ["audi","bmw","volvo","kia","byd"]
#for avto in avtolar:
#    print(avto.title())   # bizga bmw ni barchasi katta harflarda bolishi kerak 
                           #bunda faqat birinchi harf katta bilan chiqadi
                           
avtolar = ["audi","bmw","volvo","kia","byd"] 
for avto in avtolar: 
    if avto == "bmw":         # == bu tengmi? degani
                              # != bu teng emasmi? degani
       print(avto.upper())
    else:
        print(avto.title())
        
ism = input("Ismingiz nima? \n>>>")
if ism.lower() != "ali":
    print(f"Uzur {ism.lower()}, biz Alini kutayapmiz.")
else:
    print("Salom, Ali")    
    
javob = float(input("12x6 nechiga teng?>>>"))  
if javob != 72:
    print("Javobingiz xato")
else:
    print("Javobingiz to'g'ri")
    
yosh = int(input("yoshingiz nechida?>>>"))
if yosh >= 18:                               # >= bu 18 dan katta yoki tengmi degani
   print("Xush kelibsiz!")
else:
       print("Kirish mumkin emas!")    
       
login = input("Yangi login tanlang:")       
if len(login)<=5:                           # login uzunligini tekshirish
   print("Login 5 harfdan ko'proq bo'lishi kerak!")  

yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2020-yil<18:         #foydalanuvchining yoshini hisoblash    
   print(f"Yoshingiz {2020-yil}da ekan.")
   print("kirish mumkin emas!")
else:
    print("Xush kelibsiz!!!")
    
    
yoshlar = int(input("Yoshingiz nechida?>>>"))
if yosh>65:  print("Siz covid-19 risk guruhida ekansiz!")    
else: 
    print("Siz covid 19 da emas ekansiz!!!")
    

x, y = 25, 50   
print("x>y") if x>y else print("x<y")       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       