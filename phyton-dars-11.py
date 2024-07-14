# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 17:44:55 2023

@author: hp
"""
                                    
                                    # 11-dars if-elif-else


son = 50
if son <0:
    print("Manfiy son")
else:
    print("Musbat son")   
    
               # bir nechta shartlarni tekshirish kerak variantiga ko'ra 
                      #u yoki bu qiymatni chiqatishimiz kerak 
                              # elif - aks holda
                              
                              
#yosh = int(input("Yoshingiz nechida?"))
#if yosh<=4:
#    print("Sizga kirish bepul")
#elif yosh<=12:
#    print("Sizga kirish 5000 so'm")
#elif yosh<=18:
#   print("Sizga kirish 8000 so'm")    
#else:
#    print("Sizga kirish 10000 so'm") 

                     # qisqaroq qilib printni bittada yozsa ham bo'ladi


yosh = int(input("Yoshingiz nechida?"))
if yosh<=4:
    narx = 0
elif yosh<=12:
    narx = 5000
elif yosh<=18:
    narx = 8000
else:
    narx = 10000
print(f"Sizga kirish {narx} so'm")    

                                    # or - yoki
                      
kun = input("Bugun nima kun?")
if kun.lower() == "shanba" or kun.lower() == "yakshanba":
    print("Bugun dam olish kuni.")
else:
    print("Bugun ish kuni.")    


kun1 = input("Bugun nehcanchi kun?")
if kun1.lower()=="shanba" or kun.lower() == "yakshanba":
    print("Bugun dam olish kuni.")
elif kun1.lower()== "dushanba" or kun1.lower()=="seshanba" or kun1.lower()=="chorshanba" or kun1.lower()=="payshanba" or kun1.lower()=="juma":
    print("Bugun ish kuni.")
else:
   input("Siz notog'ri belgi kiritdingiz. Iltimos, hafta kunini kiriting!")    

 
                                # and - bu bo'lishi uchun barchasi true bo'lishi kerak

kun2 = input("Bugun qanday kun?")
harorat = float(input("Havo harorati qanday?"))

if kun2.lower()=="yakshanba" and harorat>=30:
    print("Cho'milgani ketdik")
elif kun2.lower()== "yakshanba" and harorat<=30:
    print("Counterga gooo!")

kun3 = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))

if (kun3.lower()=="yakshanba" or kun3.lower()=="shanba") and harorat>=30:
    print("Cho'milgani ketdik")
elif (kun3.lower()=="yakshanba" or kun3.lower()=="shanba") and harorat<=30:
    print("Counterga gooo!")

                               # boolean(ma'lumot turlari) - bir nechta shartlarni tekshirish talab qilinsa
 
narx = 15000               # mijoz 15000 so'mga taom oldi.
choy = True                # mijoz choy ham oldi
salat = False              # mizoj salat olmadi

if choy and salat:         # agar mijoz choy ham salat ham olgan bo'lsa 
    narx = narx + 10000    # narxga 10000 so'm qo'shamiz
elif choy or salat:        # agar choy yoki salat olgan bo'lsa
    narx = narx + 5000     # narxga 5000 so'm qo'shamiz
print(f"Jami {narx} so'm")    

  
narx = 15000
choy = 1     #True           # True, False ni o'rniga 1 yoki 0 qo'ysaham bo'ladi
salat = 0    #False
non = 1      #True
kompot = 1   #True
assarti = 0  #False
# Quyidagi har bir shart alohida tekshiriladi va bir-biriga bo'g'liq emas
if choy:
    print("Mijoz choy oldi.")
    narx = narx + 3000
if salat:
    print("Mijoz salat oldi.")
    narx = narx + 5000
if non:
    print("Mijoz non oldi.")    
    narx = narx + 2000
if kompot:
    print("Mijoz kompot oldi.")
    narx = narx + 5000
if assarti:
    print("Mijor assarti oldi.")    
    narx = narx + 15000
print(f"Jami {narx} so'm")


                     # in - matnni ro'yhatni ichida bormi yo'qmi tekshirish uchun

#menu = ["osh","qozonkabob","shashlik","norin","somsa"]
#"manti" in menu      # menuda manti bormi?

menu = ["osh","qozonkabob","shashlik","norin","somsa"]
ovqat = input("Nima ovqat yeysiz?>>>")
if ovqat.lower() in menu:
    print("Buyurtma qabul qilindi.")
else:
    print("Afsuski bizda bunday ovqat yo'q")    

           
                      # not in - matnni ro'yhatni ichida yo'qmi tekshirish uchun

menyu = ["osh","qozonkabob","shashlik","norin","somsa"]
ovqat1 = input("Nima ovqat yeysiz?>>>")
if ovqat1.lower() not in menyu:
    print("Buyurtma qabul qilindi.")
else:
    print("Afsuski bizda bunday ovqat yo'q") 


menu1 = ["osh","somsa","shashlik","norin""kabob"]
buyurtmalar = ["osh","somsa","manti","shashlik"]
if buyurtmalar:
   for taom in buyurtmalar:
      if taom in menu1:
          print(f"Menuda {taom} bor")
      else:
          print("Kechirasiz, menuda bunday taom yo'q!!!!!")

























                     