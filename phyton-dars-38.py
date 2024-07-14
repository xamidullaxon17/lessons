# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:04:43 2023

@author: hp
"""

#                                   38 - dars

import datetime as dt

# # datetime
# hozir = dt.datetime.now()
# print(hozir)
# # sanani ajratib olish
# print(hozir.date())
# # vaqtni ajratib olish
# print(hozir.time())
# # soatni ajratib olish
# print(hozir.hour)
# # minutni ajratib olish
# print(hozir.minute)
# # sekundni ajratib olish
# print(hozir.second)

# # date()
# bugun = dt.date.today()
# print(f"Bugungi sana: {bugun}")
# ertaga = dt.date(2023,12,21)
# print(f"Ertangi sana: {ertaga}")

# # time()
# hozir = dt.datetime.now()
# vaqtHozir = hozir.time()
# print(vaqtHozir)
# # soatni qo'lda kiritish
# vaqtKeyin = dt.time(23,45,15)
# print(vaqtKeyin)

# # sanalar orasidagi farqni topish
# bugun = dt.date.today()
# ramazonga = dt.date(2024,4,15)
# farq = ramazonga - bugun
# print(f"Ramazonga {farq.days} kun qoldi")

# # Soatlar orasidagi farq
# hozir = dt.datetime.now()
# futbol = dt.datetime(2023,12,23,20,00)
# farq = futbol-hozir
# print(farq)
# sekundlar = farq.seconds
# minutlar = int(sekundlar/60)
# print(f'{sekundlar} sekundda {minutlar} minut bor')
# soatlar = int(minutlar/60)
# print(f"Futbol boshlanishiga {farq.days} kunu {soatlar} soat qoldi.")

# # vaqtni millisekundsiz chiqaramiz
# vaqt = hozir.strftime("%H:%M:%S")
# print(f"Hozir soat: {vaqt}")

# # sanani kun-oy-yil koʻrinishida chiqaramiz
# sana = hozir.strftime("%d-%m-%Y")
# print(f"Bugun sana: {sana}")

# # sanani kun/oy/yil koʻrinishida chiqaramiz
# sana_vaqt = hozir.strftime("%d/%m/%Y, %H:%M")
# print(sana_vaqt)


import math 
# PI = math.pi
# print(f"PI ning qiymati: {PI}")
# E = math.e # natural logoriflarning asosi
# print(f"e ning qiymati: {E}")

# # trigonometriya
# math.sin(math.pi/2) # radianda 
# math.cos(0)
# math.tan(PI)

# # radianlar va burchaklar o'rtasida konvertatsiya
# print(math.degrees(math.pi/2)) # degrees - radian qiymat berganda burchakni qaytaradi
# print(math.radians(90)) # radians - aksincha, burchak berganda radianga o'girib beradi

# # logorifmlar
# # natural logorifm
# print(math.log(5))
# # 10 asosli logarifm
# print(math.log10(100))

# # sonlarni yaxlitlash
# x = 4.6
# print(math.ceil(x)) # yuqoriga yaqinlashtiradi
# print(math.floor(x)) # pastga yaqinlashtirdi
# print(round(x)) # eng yaqin butun songa yaqinlashtiradi

# # Kvadrat ildiz
# x = 81
# print(math.sqrt(x))

# # Darajaga oshirish
# math.pow(x, 3) # x ning kubi
# math.pow(x,5) # x ning 5-darajasi
# math.pow(x,1/3) # x dan kub ildiz



from pprint import pprint
import json

# filename = 'bemor_json'
# with open(filename) as f:
#     bemor = json.load(f)
# print(bemor)
# print('--------')
# pprint(bemor)

# import requests
# r = requests.get('https://api.github.com')
# pprint(r)



import re # matnlarga andoza berishga ishlatiladi
# from uzwords import words

# word1 = 'темир'
# word2 = 'томур'
# word3 = 'тулпор'

# andoza = "^т...р$"

# print(re.match(andoza,word1))
# print(re.match(andoza,word2))
# print(re.match(andoza,word3))

# matches = []
# for word in words:
#     if re.match(andoza,word):
#         matches.append(word)

# print(matches)

# # Email ajratib olish
# matn = """Maqolalar 2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
#     """
# andoza = "[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
# email = re.findall(andoza,matn) # findall matndan andozani ajratib oladi
# print(email)

# # IHateRegex bu saytdan tayyor parol, andozalar olsa bo'ladi


# andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
# msg = "Yangi parol kiriting"
# msg += '(kamida 8 belgidan iborat,kamida 1 ta lotin bosh harf,1 ta kichik harf,'
# msg += "1 ta son va 1 ta maxsus belgi bo'lishi kerak): "

# while True:
#     password = input(msg)
#     if re.match(andoza,password):
#         print("Maxfiy so'z qabul qilindi")
#         break
#     else:
#         print("Maxfiy so'z talabga javob bermaydi")





#                                       HomeWork

# 1
# haf = dt.date(2023,12,27)
# for n in list(range(10)):
#     kun = hozir + hozir.days(7)
#     hafta.append(kun)
#     print(f"{n}-hafta: {hafta}")



bugun = dt.date.today()

# hafta = []
# print(hozir)
# while range(10):
#     hafta = kun + hozir.date() 
#     print(hafta)


# 2 
bugun = dt.date.today()
ramazonga = dt.date(2024,4,15)
qurbon = dt.date(2024,7,15)
farq = ramazonga - bugun
farq1 = qurbon - bugun

print(f"Ramazonga {farq.days} kun qoldi")
print(f"Qurbon hayitiga {farq1.days} kun qoldi")                        # DONE

# 3
bugun = dt.date.today()
tkun = dt.date(2001,2,7)
vaqt = bugun - tkun
print(f"Men tug'ilganimga {vaqt} vaqt bolibdi ") # not yet done

# 4
# andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

# while True:
#       savol = input("Telefon raqamingizni kiriting ")
#       if re.match(andoza, savol):
#           print("Nomeringiz qabul qilindi")
#           break
#       else:
#           print("Notog'ri raqam kiritdingiz.")


# 5

matn = """Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI
Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. 
Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""
andoza1 = "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"

url = re.findall(andoza1,matn)
print(url)


