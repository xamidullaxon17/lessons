"""
Created on Thu Nov 16 14:22:27 2023

So'z topish o'yini

"""

#                                   SO'Z O'YINI

print("Keling o'ylagan sonni topish o'ynaymiz! ")

import random as r

def man_topaman(x=10):
    """Komputer son o'ylaydi, men topishim kerak."""
    print(f"1 dan {x} gacha son o'yladim. Topa olasizmi? ")
    taxminlar = 0
    komputer = r.randint(1, x)
    while True:   
        taxminlar += 1
        savol = int(input(">>> "))
        if savol > komputer:
            print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qilib ko'ring: ")
        elif savol < komputer:
            print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qilib ko'ring: ")
        else:
            break
    print(f"TOPDINGIZ! {komputer} sonini o'ylagan edim.{taxminlar} ta taxmin bilan topdingiz. Tabriklayman!!")    
    return taxminlar    
    


def komputer_topadi(x=10):
    """Men son o'ylayman, komputer shu sonni topishi kerak."""
    print(f"1 dan {x} gacha son o'ylang. Men topishga harakat qilaman. ")
    input("Son o'ylagan bo'lsangiz istalgan tugmani bosing. ")
    taxminlar = 0
    quyi = 1
    yuqori = x
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = r.randint(quyi,yuqori)
        else:
            taxmin = quyi
        savol = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq(-)?? ")
        if savol == "+":
            quyi = taxmin+1            
        elif savol == "-":
            yuqori = taxmin-1
        else:
            savol.lower() == 't'   
            print(f"Siz o'ylagan son {taxmin} ga teng.")
            break
    print(f"Siz o'ylagan sonni {taxminlar} ta urinish bilan topdim.")      
    return taxminlar                      




def play(x=10):
    print("Keling o'ylagan sonni topish o'ynaymiz! ", end= "")
    while True:
        schot_komp = 0
        schot_man = 0
        taxmin_maniki = man_topaman()
        taxmin_komp = komputer_topadi()
        if taxmin_komp < taxmin_maniki:
            print(f"Komputer {taxmin_komp} ta taxmin bilan topdi va yutdi.")
            schot_komp+=1
        elif taxmin_komp > taxmin_maniki:
            print(f"Siz {taxmin_maniki} ta taxmin bilan topdingiz va yutdingiz.")
            schot_man+=1
        else:
            print(f"Durrang! Ikkalamiz ham {taxmin_maniki} ta taxmin bilan topdik.")
            schot_komp+1
            schot_man+=1
        savol = int(input("Yana boshidan o'ynaysizmi? yes(1)/no(0): "))
        if savol == 0:
            break
    if schot_komp>schot_man:    
        print(f"Umumiy hisob {schot_komp}:{schot_man}. Komputer foydasiga.")
    elif schot_man>schot_komp:
        print(f"Umumiy hisob {schot_man}:{schot_komp}. Sizning foydangizga.")
    else:
        print("Do'stlik g'alaba qozondi. ")        
    return print("O'yin tugadi.")



























    



