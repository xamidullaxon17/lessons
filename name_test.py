# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 21:11:30 2023

@author: hp
"""

#                             36 - dars Funksiyalarni tekshirish
# unittest - buni yordamida turli xil funksiya,ojbjectlarni turli xil tekshirish mumkin.

# 1
# def get_full_name(ism,familiya):
#     return f'{ism} {familiya}'.title()


# 2
def get_full_name(ism,familiya,otasi = ''):
    if otasi:
        return f"{ism} {otasi} {familiya}".title() # to'g'irlangan varianti
    else:
        return f"{ism} {familiya}".title()


























