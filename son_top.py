# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:11:49 2024

@author: hp
"""


from random import randint as r

def son_top(x):
    rand = r(1,x+1)
    n = 1
    savol = int(input(f"1 dan {x} gacha son o'yladim. Topa olasizmi? "))
    while True:
        if savol > rand:
            savol = int(input("Xato, Men o'ylagan son bundan kichikroq.Yana harakat qilib ko'ring: "))
            n = n + 1
        elif savol < rand:
            savol = int(input("Xato, Men o'ylagan son bundan kattaroq.Yana harakat qilib ko'ring: "))
            n = n + 1
        elif savol == rand:
            print(f"TOPDINGIZ! {rand} sonini {n} ta urinish bilan topdingiz. Tabriklayman!!")
            break
    return n
        
# print(son_top(10))     

def pc_top(x):
    print(f"1 dan {x} gacha son o'ylang. Men topishga xarakat qilib ko'raman. ")     
    input("Son o'ylagan bo'lsangiz istalgan tugmani bosing: ")

    low = 1
    high = x
    n = 0
    while True:
        n += 1
        if low != high:
            taxmin = r(low,high)
        else:
            taxmin = low
        javob = input(f"Siz {taxmin} sonini o'yladingiz. To'g'ri (T), men o'ylagan son"
                      f"bunda kattaroq (+), yoki kichikroq (-)?? ")
        if javob == "+":
            low = taxmin + 1
        elif javob == "-":
            high = taxmin - 1
        elif javob.lower() == "t":
            print(f"Siz o'ylagan {taxmin} sonini {n} ta urinish bilan topdim!!")
            break
        else:
            en = input("O'yin to'xtatildi. davom etish uchun 'Enter' tugmasini bosing: ")
            if en:
                continue
            
    return n
    
# print(pc_top(10))     


def yanami():
    print("Keling, son top o'yinini o'ynaymiz!")
    son = int(input("Nechta songacha o'ynashni xohlaysiz? "))
    while True:
        a = son_top(son)
        b = pc_top(son)
        if a < b :
            print(f"Siz {a}:{b} hisobi bilan yutdingiz.Tabriklayman!")
        elif a > b:
            print(f"Men sizni {a}:{b} hisobi bilan yutdim!")
        elif a == b:
            print(f"Durrang! Ikkalamiz ham {a} ta urinish bilan topdik")
        yana = int(input("Yana o'ynaymizmi: Ha(1)/Yo'q(0): "))
        if yana == 1:
            continue
        else:
            break
    print("O'yin uchun rahmat!!!")

print(yanami())





