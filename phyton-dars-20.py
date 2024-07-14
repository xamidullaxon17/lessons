# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:57:44 2023

@author: hp
"""

                                   # 20 - dars

# def toliq_ism_yasa(ism, familiya, otasining_ismi=""):
#     """Toliq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()


# talaba1 = toliq_ism_yasa("olim", "hakimov")
# talaba2 = toliq_ism_yasa("hakim", "olimov", "abrorovich")
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# **********************************************************************************************

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# avto1 = avto_info("GM","Malibu","Qora","Avtomat",2018)
# avto2 = avto_info("GM","Gentra","Oq","Mexanika",2018, 15000)
# avtolar = [avto1,avto2]
# print(avto1)
# print(avto2)
# print(avtolar)
# print(avtolar[0]['model'])
# print("Onlayn bozordagi mavjud avtomashinalar: ")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = 'No\'malum'
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# **************************************************************************************

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto
# print("Saytimizdagi avtolar ro'yhatini shakllantiramiz.")
# avtolar = [] # salondagi avtolar uchun bo'sh ro'hat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rangi = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yili = input("Ishlab chiqarilgan yili: ")
#     narhi = input("Narhi: ")
#     #  Foydalanuvchi kiritgan ma'lumotlardan avto_info yordamida
#     # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya,model,rangi,korobka,yili,narhi))
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break
# print("\Salonimizdagi avtolar:")
# for avto in avtolar:
#     if avto in avtolar:
#         narh = avto['narh']
#     else:
#         narh = "No'malum"
#     print(f"{avto['rang'].title()} {avto['model'].title()}, {korobka} korobka. Narhi: {narh}")



# **************************************************************************************


# def sim(ism,familya):
#     """ism familya qaytaruvchi dastur"""
#     toliq_ism = f"{ism} {familya}"
#     return toliq_ism
# ismfam = sim('Alisher',"Odilov")
# ismfam1 = sim('Xamidullaxon',"Akromov")
# print(f'{ismfam} darsga kelmadi.\n{ismfam1} esa darsga keldi.')

# ##
# def oraliq(min,max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar
# print(oraliq(20,50))

# ### range() funksiyasini yaratdim.
# def oraliq(min,max,oraliq = 1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         if oraliq >= 2:
#             min += oraliq
#     return sonlar
# print(oraliq(20,50,3))


# **************************************************************************************


# 1 and 2
# def hammasi(ism, familya, yil, joy, email = '' , tel = None):  # None sonlarga beriladi
#                                                                # '' esa hech nma yozmasa ham boladi
#     """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumot = {
#         'ism':ism,
#         "familya":familya,
#         "yil":yil,
#         "joy":joy,
#         "email":email,
#         "telefon":tel,
#         "yoshi": 2023-yil
#         }
#     return malumot
# malumotlar = []
# while True:
#     print("\nQuyidagi ma'lumotlarin kiriting:")
#     ism = input("Ismingiz: ")
#     familyas = input("Familyangiz: ")
#     yil = int(input("Tug'ilgan yilingiz: "))
#     joy = input("Tug'ilgan joyingiz: ")
#     email = input("Emailingiz: ")
#     tel = input("Telefoningiz: ")
#     malumotlar.append(hammasi(ism,familyas,yil,joy,email,tel))
#     javob = input("Yana ma'lumot qo'shasizmi?(yes/no) ")
#     if javob == 'no':
#         break
# print("Hamma haqidagi ma'lumotlar:")
# for malumot in malumotlar:
#         print(f"{malumot['ism'].title()} {malumot['familya'].title()},{malumot['yil'], {malumot['joy']}"
#         f"{malumot['yoshi']} yoshda, telefoni: {malumot['telefon']}")
        
#  3
# def son_info(s1,s2,s3):
#     '''Sonlarni eng kattasini qaytaruvchi dastur'''
#     max = s1
#     if s2 >= max:
#         max = s2
#     if s3 >= max:
#         max = s3
#     return max

# s = son_info(5,10,15)
# print(s)

# 4
# def radiusi(r,PI = 3.14):
#     """Radiusini aniqlaydigan funksiya"""
#     aylana = {
#                 "radiusi": r,
#                 'diametri': r/2,
#                 'perimetri': 2*PI*r,
#                 'yuzi': PI*(r**2)
#                 }
#     return aylana
# rad = radiusi(55)
# print(rad)

# # 5
# def tub_sonlar_top(min, max):
#     '''Tub sonlarni qaytaruvchi funksiya'''
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#     return tub_sonlar
# a = tub_sonlar_top(1,5)
# print(a)

# 6
def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    return sonlar
print(fibonacci(10))
#2....1+0   3....2+1   5....3+2    8....5+3





