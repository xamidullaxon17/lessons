# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 00:46:26 2023

@author: hp
"""

def getArea(r,pi=3.14159):
    """Doiraning yuzini qaytaruvchi funksiya"""
    return pi*(r**2)

def getPerimetr(r,pi=3.14159):
    """Doiraning perimetrini qaytaruvchi funksiya"""
    return 2*pi*r

#                                   HomeWork
# 1
def son(a,b,c):
    if a < b > c:
        return b
    if b < a > c:
        return a
    if b < c > a:
        return c

# 2 
def matn(matnlar):
    matnla = []
    for mat in matnlar:
        matnla.append(mat.title())
    return matnla

# 3 
def juftmi(sonlar):
    sonla = []
    for son in sonlar:
        if not (son % 2):
            sonla.append(son)
    return sonla

# 4 
def fibonacci(n):
    sonlar = []
    for x in range(100):
        if x == 0 or x == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x - 1] + sonlar[x - 2])
    fibo_soni = []
    for son in sonlar:
        if son == n:        
            fibo_soni.append(son)
    if fibo_soni:
        return True
    else:
        return False

    











































