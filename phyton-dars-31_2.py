# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:16:43 2023

@author: hp
"""

from avto import Avto

avto1 = Avto("GM","Malibu","Qora",2020,40000,1000) 
avto2 = Avto("GM","Cobalt","Oq",2022,15000)
avto3 = Avto("GM","Gentra","Qora",2020,20000,1500)
print(avto1.narh)
print(Avto.get_num_avto())


from uuid import uuid4
class Shaxs:
    """"Shaxslar haqida ma'lumot"""
    __num_people = 0
    def __init__(self,ism,familiya,passport,tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.t_soni = 0
        self.__uuid = uuid4()
        Shaxs.__num_people += 1
    
    @classmethod
    def get_human(cls):
        return cls.__num_people
    
    def get_talaba(self):
        self.t_soni += 1
        return self.t_soni
    
    def get_value(self):
        return self.__uuid
    
    def set_value(self):
        return self.__uuid
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f'{self.ism} {self.familiya}. '
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ilgan."
        return info
    def get_age(self,yil):
        """Shaxning yoshini qaytaruvchi metod"""
        return yil - self.tyil

# consolda qilindi
inson2 = Shaxs("Alisher","Odilov","AV433438",2000)
inson = Shaxs("Xamidullaxon","Akromov","AB6111499",2001)
inson.get_info()            
inson.get_age(2023)




class Talaba(Shaxs): # Shaxs - super class. Talaba - voris class
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiytatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1 
        self.manzil = manzil
        self.fanlar = []
        self.__uuid = uuid4()
        
    def get_ad(self):   
        return self.__uuid
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}."
        return info
    
    def fanga_yozil(self,student):
        """Fanlarga qo'shish"""
        self.fanlar.append(student)
        
    def remove_fan(self,kerakmas):
        if not self.fanlar:
            print("Siz bu fanga yozilmagansiz.")
        else:
            self.fanlar.remove(kerakmas)
        return self.fanlar
    
    