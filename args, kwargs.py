# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 02:24:26 2024

@author: hp
"""

#    *args, **kwargs

def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi
print(summa(2,4,5))


def sonlar(*son):
    sonla = 1
    for s in son:
        sonla*=s
    return sonla
print(sonlar(3,23,45,3,23,4,452,23,32))


def talaba(ism,familiya,**malumot):
    malumot['ismi'] = ism.title()
    malumot['familiyasi'] = familiya.title()
    return malumot
talaba1 = talaba("xamidullaxon","akromov",yili=2001,t_joy="Uzbekistan")
talaba2 = talaba("bobur","akromov",yili=2000,t_joy="Uzbekistan")

print(talaba2)


# from all_lessons import bahola as bh


# import all_lessons
# a = ['alisher','vali','xamid','behzod']

# b = all_lessons.bahola(a)
# print(b)


from random import randint as r , choice as ch, shuffle  as sh
son = r(3, 300)
print(son)

matn = ['alisher','vali','xamid','behzod']
tanla = ch(matn)
print(tanla)
print(ch(tanla))

rand = list(range(1,10))
print(rand)
sh(rand)
print(rand)






















