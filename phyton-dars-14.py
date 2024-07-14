# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:40:33 2023

@author: hp
"""

                      # Dictionary (Lug'at)
                      

car_0 = {'model':'ferrari','rang':'qizil','tezligi':'400 km/soat'}
print(car_0['model'])                      
print(car_0['rang'])
print(car_0['tezligi'])


en_uz = {'apple':'olma','apricot':'o\'rik','banana':'banan'}
print(en_uz['apricot'])
print(en_uz)
print(en_uz['apple'])


mevalar = {'olma':10000,'tarvuz':8000,'qovun':10000}
print(f"Olma narxi {mevalar['olma']} so'm")

talaba = {'ism':'xamidullaxon',
          'yosh':'22',
          'yili':'2001'
          }
print(f"{talaba['ism'].title()},\
      {talaba['yili']}-yilda tug'ilgan,\
      yoshi esa {talaba['yosh']}da")
      
# yangi kalit qo'shish talaba ga

talaba['kurs'] = 3
talaba['fakultet'] = 'matematika'
talaba['yo\'nalishi'] = 'matematika'
# ism ni ozgartirish uchun
talaba['ism'] = 'begzod'
print(talaba)


talaba_1 = {}
talaba_1['ism'] = "Nodir"
talaba_1['familya'] = "Axedov"
talaba_1['kurs'] = 3
talaba_1['yo\'nalishi'] = "Matematika"
print(talaba_1)

# lugatdan kalitni o'chirish

del talaba_1['familya']
print(talaba_1)

telefonlar = {
    'ali':'samsung',
    'vali':'samsung',
    'g\'ani':'apple'
    }
#print(telefonlar)

# get metodi - agar ro'yhatda bo'lmasa shunday natijani chiqaradi

phone = telefonlar.get('hasan','Bunday ism mavjud emas!')
print(phone)


                       # davomi 15- dars
                       
print(talaba.items())  # barcha lug'atlardagilarni chiqarib beradi
for key,value in talaba.items():
    print(f"kalit: {key}")                       
    print(f"qiymat: {value}\n")

for ism,marka in telefonlar.items():
    print("Ismi",ism)
    print("Markasi", marka)

# yana boshqacharo'g'i

for k,q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")
    
                     # lug'at ichidagi har bir kalitni qaytaradi
                     
mahsulotlar = {
    'olma':10000,                   
    'anor':20000,
    'uzum':30000,
    'anjir':40000,
    'shaftoli':25000,
    'behi':30000
    }

print(mahsulotlar.keys())

print("Do'kondagi mahsulotlar")
#for mahsulot in mahsulotlar.keys():
#   print(mahsulot.title())

bozorlik = ['anor','uzum','behi','baliq','non']
for mahs in mahsulotlar:
    if mahs in bozorlik:
        print(f"{mahs.title()} {mahsulotlar[mahs]} so'm")

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, {buyum} ham olib keling!")

                       
 
                       # lug'atlarni sorted() yordamida alifbo tartibida joylash

for ben in sorted(mahsulotlar):
    print(ben.title())
     
                      # faqat qiymatini chiqarish uchun values()
                      
print(telefonlar.values())                      

print("Foydalanuvchilar shu markadan foydalanadilar:")
for tel in telefonlar.values():
    print(tel)

gadjetlar = {
    'ali':'samsung',
    'vali':'samsung',
    'g\'ani':'apple',
    'xami':'redmi note 11 pro',
    'begi':'mi',
    'xusan':"motorolla"
    }


                      #     set() 2 ta bir xil elementlarni takrorlanmagan holda chiqarish                   

print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
for gad in set(gadjetlar.values()):
    print(gad.title())
    
# set() bu ma'lumot turlaridan biri

toys = {'ball','car','lamp','ball','ball','ball','ball'}
print(toys)  # bir xil ma'lumotni chiqarib tashlaydi












