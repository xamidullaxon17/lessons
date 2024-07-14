# # -*- coding: utf-8 -*-
# """
# Created on Fri Aug 25 20:58:16 2023

# @author: hp
# """

#                          # List - ro'yhatlar []
                         
# mevalar = ['olma','anjir','shaftoli',"o'rik"]
# narxlar = [12000,18000,10900,22000]
# sonlar = ['bir','ikki',3,4,5]
# ismlar = []
# print(mevalar[1])
# print(mevalar[-2])                        
# print(sonlar[1].title())
# print(narxlar[1]+narxlar[3])


# mevalar[1] = 'nok'
# print(mevalar[1])

#                                # .append() - list oxiriga qo'shadi

# mevalar.append('tarvuz')
# print(mevalar)                               

#                                # .insert() - listni xohlagan joyiga qo'shish
                              
# mevalar.insert(1, "banan")
# print(mevalar)         

# cars = []
# cars.append("Lasetti")
# cars.append("Nexia")
# cars.append("Cobalt")
# cars.append("Spark")
# print(cars)

#                             # del - elementlarni o'chirish
                            
# del cars[0]
# print(cars)   
                         
                            

#                            # .remove() - tanlab elementni o'chirib tashlash
                           
# cars.remove("Spark")                         

 
#                            # .pop() - yordamida elementlarni sug'urib olish
                           
# bozorlik = ["yog'","un","piyoz","go'sht","banan"]
# mahsulot = bozorlik.pop(1)                         
# print(bozorlik)                           
# print(mahsulot)       
# print("Men bozordan", mahsulot , "sotib oldim.\nAmmo", bozorlik, "bularni esa olish esimdan chiqib qopti")
  
                            






#                                    ######### 8-dars davomi       
                           
#                           # Ro'yhatni alifbo tartibida joylash
                                
#                                   # .sort()
# cars = ["BMW","Mercedes Benz","Volvo","Lamborghini","Bugatti","Ferrari", "McLaren","Audi","BYD"]
# #cars.sort()
# #print(cars)
 
#                           # alifboni teskarisiga taxlash uchun
                        
#                                    #.sort(reverse=True)
                                   
# #cars.sort(reverse=True)
# #print(cars)                                   
                          
#                           # asl ro'yhatga tegmagan holda tartiblangan ro'yhatni chiqarish
                                           
#                                            # sorted()
                              
# #print(sorted(cars, reverse=True))                                         
  
# sonlar = [12, 52, 58, 42, 36, -51, 1,25,91,-2,0,1,-5]
# print(sorted(sonlar))
# sonlar.sort()
# print(sonlar)
# sonlar.sort(reverse=True)
# print(sonlar)

#                          # listni o'rnini almashtirish teskarisi
                         
#                                   # .reverse()
# cars.reverse()
# print(cars)                                     
                            
#                          # ro'yhatning sonini aniqlash
                              
#                                  # len()
                                 
# print(len(sonlar))
# uzunlik = len(cars)
# print(uzunlik)


#                          # elementlarni orasidagini chiqatib beradi     
 
#                               # range(**,**)

# sonlar = list(range(0,25))
# print(sonlar)
# sinflar = list(range(12,30))
# print(sinflar)

# toq_sonlar = list(range(1,20,2))
# print(toq_sonlar)
# juft_sonlar = list(range(0,20,2))
# print(juft_sonlar)
# sanash = list(range(0,101,10))
# print(sanash)
 
#                                   # maximum qiymatini topish
                                  
#                                         # max()  # min()  # sum() yigindisi
                                        
# max_qiymat = max(toq_sonlar)
# print(max_qiymat)                                        
# min_qiymat = min(toq_sonlar)
# print(min_qiymat)    
# sum_qiymat = sum(toq_sonlar)
# print(sum_qiymat)    


# brands = ["BMW","Mercedes Benz","Volvo","Lamborghini","Bugatti","Ferrari", "McLaren","Audi","BYD"]
# print(brands[1:4])    #  ['Mercedes Benz', 'Volvo', 'Lamborghini']  wunaqa chiqadi

# #my_cars = brands
# #my_cars.remove("Volvo")
# #print(my_cars)
# #my_cars[7] = "Chiron"
# #print(my_cars)

# my_cars = brands[:] # barchasini oladi brands listidan ammo brands listidagilar o'zgarmaydi
# print(my_cars)
# my_cars.remove("BYD")


                                # o'zgarmas ro'yhat ()
                                
                                # tuple() 
                               
toys =("bus","barbie","car","ball","teddy")  # buni ichidagilarni o'zgartirib bo'lmaydi
print(toys)
toys = list(toys)          # ichidagilarni o'zgartirish uchun listga o'tkaziladi
toys.append("snake")       # element qo'shildi
toys = tuple(toys)         # endi listni qaytarib o'zgarmas qilish uchun tuple ishlatiladi
print(toys)





















    