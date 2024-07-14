# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 19:06:07 2023

@author: hp
"""

#                                       31 - Dars Inkapsulatsiya

from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.__km = km
        self.__uuid4 = uuid4()
    
    def get_km(self):
        return self.__km
    
    def get_num(self):
        return self.__uuid4
    
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km += km
        else:
            print("Mashinaning km ni kamaytirib bo'lmaydi.")

avto1 = Avto("GM","Malibu","Qora",2020,40000,1000) 
