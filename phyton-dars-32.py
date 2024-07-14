# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 17:24:24 2023

@author: hp
"""

#                           32 - Dars Dunder metodlari

# dir(Avto)  dunderlarni ko'rish uchun 

class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.narh = narh
        Avto.__num_avto += 1

    def __repr__(self): # objectga murojat qilganda qandaydir ma'lumot qaytaradi. (print(avto1))
        return f"Avto: {self.make} Model: {self.model}"
    # str(avto1)
    def __str__(self):  # __repr__ ga o'xshab bir xil vazifani bajaradi.
        return f"Avto: {self.make} Model: {self.model}"
    # repr(avto1)
    
    def __eq__(self,y): # == tengmi ikkita objectni taqqoslash.  avto1==avto2 or avto1 != avto2
        return self.narh == y.narh
        
    def __lt__(self,y): # < yoki > ligini taqqoslash.   avto1<avto2  or  avto1>avto2
        return self.narh < y.narh
    
    def __le__(self,y): # <= yoki >= ligini taqqoslash.  avto1 >= avto2  or avto1 <= avto2
        return self.narh <= y.narh
    
class AvtoSalon:
    """AvtoSalon"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self): # uzunligini ko'rish len(salon1)
        return len(self.avtolar)
    
    def __getitem__(self,index): # indexini chaqirganda malumot chiqaradi. salon1[1] 
        return self.avtolar[index]
    
    def __setitem__(self,index,qiymat): # indexdagi objectni yangi berilgan qiymat ga o'zgartiradi. salon1[0] = Avto("BMW","X7","Qora",2020,150000)
        self.avtolar[index] = qiymat
        
    # def __call__(self): # objectni caqiradi shunday yozganda: salon1()
    #     return [a for a in self.avtolar]
    
    def __call__(self,*qiymat): # salon1(avto1,avtoq2,avto3) salon1 ga qo'shadi.
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [a for a in self.avtolar]
        
    def __add__(self,y): # ikkita salonni bir biriga qo'shish. salon3 = salon1 + salon2
        if isinstance(y,AvtoSalon):
            yangi_salon = AvtoSalon(f"{self.name} {y.name}")
            yangi_salon.avtolar = self.avtolar + y.avtolar
            return yangi_salon            
        elif isinstance(y,Avto):
            self.add_avto(y)
            
    def add_avto(self,*qiymat): # salon1.add_avto(avto1,avto2,avto3)
        for x in qiymat:
            if isinstance(x,Avto):  # bu degani x degan object Avto degan klassda bormi
                self.avtolar.append(x)
            else:
                print("Avto kiriting")
        
salon1 = AvtoSalon("MaxAvto")   
salon2 = AvtoSalon("Avto Lider")

avto1 = Avto("GM","Malibu","Qora",2020,40000)      
avto2 = Avto("GM","Lacetti","Oq",2020,20000)
avto3 = Avto("Toyota","Corolla","Silver",2018,45000)
salon1.add_avto(avto1,avto2,avto3)

avto4 = Avto("Mazda","S5","Qizil",2020,35000) 
avto5 = Avto("Lamborghini","Urus","Sariq",2015,300000) 
avto6 = Avto("BMW","X7","Qora",2019,150000) 
salon2(avto4,avto5,avto6)
# Operator over low - operatorlarni tanqil qilish










