# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 16:15:34 2023

@author: hp
"""


#                                           30 - Dars


# Vorislik - bir classdan boshqa bir class yaratish
# Polimorfizm - yangi yaratilgan classni ishida super classdan meros qolgan birorbir metodni o'zgartirish

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

# consolda qilindi
inson = Shaxs("Xamidullaxon","Akromov","AB6111499",2001)
inson.get_info()            
inson.get_age(2023)

class Professor(Shaxs):
    """Professor nomli klass"""
    def __init__(self,ism,familiya,passport,tyil,oyligi,vazifasi):
        """Proffessorning xususiyatlari"""
        super().__init__(ism,familiya,passport,tyil)
        self.oyligi = oyligi
        self.vazifasi = vazifasi
    
    def get_salary(self):
        """Oyligi"""
        return self.oyligi
    
    def get_worked(self):
        """Vazifasi"""
        return self.vazifasi
    
    def get_malumot(self):
        """Ma'lumot"""
        return f"{self.ism} {self.familiya}ning oylik maoshi - {self.oyligi}."
ishchi = Professor("Xamidullaxon", "Akromov","AB6111499",2001,15000000,"oylik hisoblash")  

class Foydalanuvchi(Shaxs):
    """Foydalanuvchi klassi"""     
    def __init__(self,ism,familiya,passport,tyil,maqsadi):
        """Foydalanuvchi"""
        super().__init__(ism,familiya,passport,tyil)
        self.maqsadi = maqsadi
        
    def get_maqsad(self):
        """Maqsadi"""
        return self.maqsadi
    
ishchi1 = Foydalanuvchi("Alisher", "Komilov", "BD2w4532", 2002, "Bilim olish")    
    
class Man(Foydalanuvchi):
    """O'zim haqimda ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil,maqsadi,lavozimi):
        """O'zim  haqimda"""
        super().__init__(ism,familiya,passport,tyil,maqsadi)
        self.lavozimi = lavozimi
        
    def get_men(self):
        return self.lavozimi
    
    def ban_user(self,block):
        return f"Foydalanuvchi {self.ism} bloklandi."
    
class Lavozimim:
    """Maqsadim"""
    def __init__(self,lavozim):
        self.maqsadim = lavozim
    def get_maqsadim(self):
        return self.lavozim

lavozimi = Lavozimim("Dunyodagi barcha narsalarga egalik qilish")    
men = Man("Xamidullaxon","Akromov","AB6111499",2001,"Millioner bo'lish",lavozimi)    
    
        
        
class Talaba(Shaxs): # Shaxs - super class. Talaba - voris class
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """Talabaning xususiytatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1 
        self.manzil = manzil
        self.fanlar = []
    
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
        
class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self,uy,kocha,tuman,viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""      
        manzil = f"{self.viloyat.title()} viloyati, {self.tuman.title()} tumani, "
        manzil += f"{self.kocha.title()} ko'chasi, {self.uy}-uy."
        return manzil

talaba1_manzil = Manzil("9a","xadra","shayhontohur","toshkent shahar")
talaba1 = Talaba("Alisher","Giyosov","AB61134494",2004,"NO5197907",talaba1_manzil)
# consolda qilindi 
talaba1.get_info()
talaba1.manzil.get_manzil()
        

class Fan:
    """Fan klassi"""
    def __init__(self,fan):
        self.fan = fan

    def get_fan(self):
        return self.fan

fan1 = Fan("Matematika")
fan2 = Fan("Fizika")
fan3 = Fan("Kimyo")
fan4 = Fan("Adabiyot")









































