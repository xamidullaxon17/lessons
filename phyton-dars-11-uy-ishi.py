# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 02:01:49 2023

@author: hp
"""

                               # 11-dars
                               
son = int(input("Juft son kiriting: "))
if son%2 ==0:
    print("Rahmat!")
else:
    print("Bu juft son emas!")    


yosh = int(input("Yoshingizni kiriting:"))   # yosh = int(input("Yoshingizni kiriting:"))
if yosh<=4 or yosh>=60:                      # if yosh<=4 or yosh>=60: 
    print("Sizga bepul.")                    #     narx = 0:
elif yosh<=18 and yosh>=5:                   # elif yosh<18:  
    print("Sizga 10000so'm")                 #     narx = 10000
elif yosh>=18 and yosh<=59:                  # else: 
    print("20000 so'm")                      #     narx = 20000
                                             # print(f"Chipta {narx} so'm")



print("Ikkita son kiriting>>> ")
son1 = float(input("birinchi sonni kiriting:"))
son2 = float(input("ikkinchi sonni kiriting:"))
if son1>son2:
    print((f"{son1}>{son2}"))
elif son1<son2:
    print((f"{son1}<{son2}")) 
else:
    print((f"{son1}={son2}"))    


mahsulotlar = ["mandarin","apelsin","nok","anor","kivi","uzum","joxori","o'rik","banan","olma"]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:"))
if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")











                               