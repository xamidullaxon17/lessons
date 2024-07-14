# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:16:02 2023

@author: hp
"""

#                   38 - dars classlarni tekshiruvchi testlar 

class Car:
    def __init__(self,make,model,year,km=0,price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km
    
    def set_price(self,price):
        self.price = price
    
    def add_km(self,km):
        if km>=0:
            self.__km += km
        else:
            raise ValueError("km manfiy bo'lishi mumkin emas") # agar foydalanuvchi manfiy son kiritsa,...
    
    def get_model(self):
        return self.model.title()
    
    def get_year(self):
        if self.year >= 2022:
            return self.year
        else:
            raise ValueError('Yili 2022-yildan past mashinalarni qabul qilmaydi.')
    
    def get_make(self):
        return self.make
    
    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()},"
        info += f"{self.year}-yil, {self.__km} km yurgan"
        if self.price:
            info +=f"Narhi:{self.price}"
        return info
    
    def get_km(self):
        return self.__km






















