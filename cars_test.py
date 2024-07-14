# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:25:11 2023

@author: hp
"""

#                                   37 - dars

import unittest
from cars import Car

class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""
    
    def setUp(self): # setUp bu bor metod
        make = "GM"
        model = "Malibu"
        year = 2023
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make,model,year)
        self.avto2 = Car(make,model,year,price=self.price)
        
    def test_create(self):
        # Qiymatning mavjudligini assertIsNotNone metodi bilan tekshirish
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        # self.assertEqual(self.model,self.avto1.model) # bu agar funksiya xato yozilib ketsa tekshirush uchun 
        self.assertIsNotNone(self.avto1.year)
        # Qiymat mavjudligini assertIsNone metodi bilan tekshirish
        self.assertIsNone(self.avto1.price)
        # Qiymatning tengligini assertEqual metodi bilan tekshirish
        self.assertEqual(0,self.avto1.get_km())
        # avto2 narhini tekshirish
        self.assertEqual(self.price,self.avto2.price)
        
    def test_set_price(self):
        self.avto2.set_price(45000)
        self.assertEqual(45000,self.avto2.price)
        
    def test_add_km(self):
        #1 Musbat qiymat berib ko'ramiz
        self.avto1.add_km(self.km)
        self.assertEqual(self.km,self.avto1.get_km())
        self.avto1.add_km(5000)
        self.assertEqual(15000,self.avto1.get_km())
        #2 Manfiy qiymat berib ko'ramiz
        new_km = -5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
    
    def test_set_model(self):
        self.assertEqual(self.avto1.get_model(),self.avto1.model)
        
    def test_year(self):
        self.assertTrue(self.avto1.year,self.avto1.get_year())
    
    def test_get_make(self):
        self.assertEqual(self.avto2.make,self.avto2.get_make())
            
    def test_get_info(self):
        info = f"{self.avto1.make.upper()} {self.avto1.model.title()},"
        info += f"{self.avto1.year}-yil, {self.km} km yurgan"
        self.assertEqual(info,f"{self.avto1.make.upper()} {self.avto1.model.title()},{self.avto1.year}-yil, {self.km} km yurgan")
        
        
unittest.main()
        
        
        
        
        












