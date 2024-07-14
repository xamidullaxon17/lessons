# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:04:07 2023

@author: hp
"""
#                                   31 - dars davomi

from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.narh = narh
        self.__km = km
        self.__uuid4 = uuid4()
        Avto.__num_avto += 1
        
    @classmethod 
    def get_num_avto(cls):
        return cls.__num_avto
    
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
avto2 = Avto("GM","Cobalt","Oq",2022,15000)
avto3 = Avto("GM","Gentra","Qora",2020,20000,1500)