# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 23:54:36 2023

@author: hp
"""

#                                       29 - dars

class Talaba:
    """Talaba nomli klass yaratamiz"""

    def __init__(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        
        
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya

    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        """Talabaning yoshini qaytaradi"""
        return yil - self.tyil

    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")
        
    def set_bosqich(self,yangi_bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich

    def update_bosqich(self):
        """Talabaning bosqichini 1 taga ko'paytirish"""
        self.bosqich += 1



class Fan():
    """Fan nomli klass"""
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
    
    def add_student(self,talaba):
        """Fonga talabalar qo'shiladi"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1 
        
    def get_name(self):
        """Fan nomi"""
        return self.nomi

    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [talaba.get_fullname() for talaba in self.talabalar]
    
    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni

matematika = Fan("Oliy matematika")
talaba1 = Talaba("Alijon", "Valiyev", 2000)
talaba2 = Talaba('Xamidullaxon', 'Akromov', 2001)
talaba3 = Talaba("Alisher", "Axmedov", 2008)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)
# print(talaba1.get_fullname())
# print(talaba1.get_age(2021))
# print(talaba2.set_bosqich(2))
# print(talaba2.get_info())
print(matematika.get_students())



# dir(Talaba) funksiyasi - turli xil metodlar chiqib keladi. 
# __**__ - bu Dunder metodlari deyiladi.

# __**__ bular bo'lmagan metodlarni chiqarish uchun:
# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# Talaba.__dict__ - bu Talaba ga tegishli bo'lgan xususiyatlarini va uning qiymatlarini lug'at ko'rinishida qaytaradi.
# Talaba.__dict__.keys() - faqat kalit sozlarini chiqarib beradi


#                                   HomeWeork

class Avto:
    def __init__(self,model,rang,korobka,narh):
        """Xususiyatlarini qaytaradi"""
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.yurgani = 0

    def get_model(self):
        """Modeliniqaytaradi"""
        return self.model
    
    def get_color(self):
        """Rangini qaytaradi"""
        return self.rang
    
    def get_box(self):
        """Korobkasini qaytaradi"""
        return self.korobka
    
    def get_narh(self):
        """Narhini qaytaradi"""
        return self.narh + "dollar"
    
    def get_distance(self):
        """Qancha yurganini korsatadi"""
        return self.yurgani
    
    def get_info(self):
        """Avto haqida ma'lumot"""
        return f"Model- {self.model}\nRangi - {self.rang}\nKorobkasi - {self.korobka}\nNarhi - {self.narh}\nYurgani - {self.yurgani} km."      
    
    def set_update_km(self,new_km):               
        """Yurganini yangilaydi"""
        self.yurgani = new_km
        
        
class Avtosalon:
    
    def __init__(self,c_name,address,car,price):
        """Avtosalon haqida ma'lumot"""
        self.c_name = c_name
        self.address = address
        self.car = car
        self.price = price
        self.cars = []
        self.many = 0        
    def c_name(self):
        return self.c_name
    def address(self): 
        return self.address       
    def car(self):
        return self.car    
    def price(self):
        return self.price
           
    def add_cars(self,mashina):
        """Yangi avtolar qo'shish"""
        self.cars.append(mashina)
        self.many += 1
        
    def all_cars(self):
        return self.cars
        
    def car_news(self):
        """Mashina haqida ma'lumot"""
        return [x.add_cars() for x in self.cars]
    
    def get_news(self):
        """Avtolar haqida ma'lumot"""
        print(f"{self.c_name} nomli avtosalonimiz {self.address}da joylashgan bo'lib, {self.cars} turdagi avtomobillarimiz mavjud.")
    
    # def all_cars(self):
    #     return [mashina.c_name() for x in self.cars]

car1 = Avto("Bugatti","Qora","Avtomat","17 mln ")
car2 = Avto("Lamborghini","Qizil","Avtomat","4 mln ") 
car3 = Avto("Porsche","Jigarrang","Avtomat","350000 ")
car4 = Avto("Rolce Royce","Oq","Avtomat","10 mln ")
car5 = Avto("Mercedes-Benz","Qora","Avtomat","500000 ")
car1.set_update_km(100)
print(car1.get_info())


salon1 = Avtosalon("Avenue motors","Vogzal s5 ","Bugatti","17 mln")
print(salon1.add_cars(car1.model))
print(salon1.cars)
            
    































