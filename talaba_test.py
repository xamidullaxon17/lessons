# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:28:31 2023

@author: hp
"""

#                                   Homework 37 - dars

class Shaxs:
    """"Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
    
    def get_ism(self):
        return self.ism.title()
    
    def get_familiya(self):
        return self.familiya.title()
    
    def get_fullname(self):
        return f"{self.ism.title()} {self.familiya.title()}"
    
    def get_passport(self):
        return self.passport
    
    def get_tyil(self):
        return self.tyil
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f'{self.ism} {self.familiya}. '
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ilgan."
        return info
    def get_age(self,yil):
        """Shaxning yoshini qaytaruvchi metod"""
        return int(yil) - self.tyil



# class Talaba(Shaxs): # Shaxs - super class. Talaba - voris class
#     """Talaba klassi"""
#     def __init__(self,ism,familiya,passport,tyil,idraqam):
#         """Talabaning xususiytatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1 
#         self.fanlar = []
    
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}. "
#         info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}."
#         return info
    
#     def fanga_yozil(self,student):
#         """Fanlarga qo'shish"""
#         self.fanlar.append(student)
        
#     def remove_fan(self,kerakmas):
#         if not self.fanlar:
#             print("Siz bu fanga yozilmagansiz.")
#         else:
#             self.fanlar.remove(kerakmas)
#         return self.fanlar







