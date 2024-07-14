# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 19:11:40 2023

@author: hp
"""

#                                   32 - dars homework
class Shaxs:
    """"Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f'{self.ism} {self.familiya}. '
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug'ilgan."
        return info
    def get_age(self,yil):
        """Shaxning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
    def __repr__(self):
        return f"{self.ism} {self.familiya}"
    


# consolda qilindi
inson = Shaxs("Xamidullaxon","Akromov","AB6111499",2001)
inson.get_info()            
inson.get_age(2023)
 
class Talaba(Shaxs): # Shaxs - super class. Talaba - voris class
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        """Talabaning xususiytatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1 
        self.fanlar = []
    
    def __repr__(self):
        return f"{self.ism} {self.familiya} {self.tyil}"
       
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def set_bosqich(self,y):
        self.bosqich = y

    def __eq__(self,talaba): # ==
        return self.bosqich == talaba.bosqich
    
    def __lt__(self,katta): # <
        return self.bosqich < katta.bosqich
    
    def __le__(self,katta_teng): # <=
        return self.bosqich <= katta_teng.bosqich
    
    
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

talaba1 = Talaba("Alisher","Giyosov","AB61134494",2004,"NO5197907")
talaba2 = Talaba("Xamidullaxon","Akromov","AB6111499",2001,"NO12345678")

class Fan:
    def __init__(self,fan):
        self.fan = fan
        self.talabalar = []
        
    def get_talabalar(self):
        return self.talabalar

    def __setitem__(self,index,items):
        self.talabalar[index] = items
        
    def __getitem__(self,index):
        return self.talabalar[index]
    
    def __repr__(self):
        return f"{self.fan.title()}"
    
    def __len__(self):
        return len(self.talabalar)
    
    def __call__(self):
        return f"{self.fan.title()} fani bilim olish uchun."


    def add_student(self,*talaba):
        for talab in talaba:
            if isinstance(talab,Talaba):    
                self.talabalar.append(talab)
    def __add__(self,y): # ikkita salonni bir biriga qo'shish. salon3 = salon1 + salon2
        if isinstance(y, Talaba): 
            self.add_student(y)
            
            
    # def set_remove(self,y):
    #     return self.talabalar.remove(y)                
    # def __sub__(self,y): # ayirish
    #     if isinstance(y, Fan): 
    #         self.set_remove(y)
# pasdagi bilan tapadagi bir xil, faqat tepadagida talabani olib tashlaydi. pasdagida esa id raqamni olib tashlaydi.           
    def set_removed(self,y):
        return self.idraqam.remove(y)                
    def __sub__(self,y): # ayirish
        if isinstance(y, Talaba): 
            self.set_remove(y)
        
    # def fizika(self):       
    #     for x in self.fan:
    #         if x == "fizika":
    #             return x
            
        
fan1 = Fan("adabiyot")    
fan2 = Fan("Matem")            
fan3 = Fan("fizika") 
fan4 = Fan("kimyo")


    





