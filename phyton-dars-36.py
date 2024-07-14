# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 00:20:07 2023

@author: hp
"""

# import unittest  # test xatolarni tekshirish uchun
# from name_test import get_full_name

# 1
# class NameTest(unittest.TestCase): # bu shablon
#     def test_toliq_ism(self): # tekshirish har doim test bilan boshlanish kerak
#         name = get_full_name("xamidullaxon","akromov")
#         self.assertEqual(name,"Xamidullaxon Akromov") # aynat tengligini tekshirish metodi

# unittest.main() # bu NameTest ni chaqiradi va funksiyani bajaradi

# 2
# class NameTest(unittest.TestCase): # bu shablon
#     def test_toliq_ism(self):
#         name = get_full_name("xamidullaxon","akromov")
#         self.assertEqual(name,"Xamidullaxon Akromov")
        
#     def test_otasining_ismi(self):
#         name = get_full_name('xamidullaxon', "akromov",'boburovich')
#         self.assertEqual(name, 'Xamidullaxon Boburovich Akromov') # xato chiqadi va name_test moduliga o'tib .title() ni qoshish kerak.

# unittest.main()

# 3
# import unittest
# from circle import getArea, getPerimetr

# class CircleTest(unittest.TestCase):
#     def test_area(self):
#         self.assertAlmostEqual(getArea(5),78.53975,4) # oxirgi 4 - aniqligini 4 xonagacha tekshiradi.                                                     
#         self.assertAlmostEqual(getArea(10),314.159) # agar aniqligini bermasa, aniqligini 7 xonagacha tekshiradi.  
#     def test_perimetr(self):
#         self.assertAlmostEqual(getPerimetr(10), 62.8318)    
#         self.assertAlmostEqual(getPerimetr(4), 25.13272)
        
# unittest.main()


#                               HomeWork
import unittest


# 1
from circle import son
class HigherTest(unittest.TestCase): 
    def test_higher(self):
        soon = son(2,5,40)
        self.assertEqual(soon,40)        
unittest.main()        

# 2
from circle import matn
class KattaTest(unittest.TestCase):
    def test_katta(self):
        soz = matn(['olma', 'anor', 'behi', 'uzum', 'nok'])
        self.assertEqual(soz,['Olma', 'Anor', 'Behi', 'Uzum', 'Nok'])
unittest.main()

# 3
from circle import juftmi
class FuftmiTest(unittest.TestCase):
    def test_juftmi(self):
        self.assertEqual(juftmi([2,5,34,23,45,56,34,324,56,3]),[2,34,56,34,324,56])
unittest.main()

# 4
from circle import fibonacci
class FiboTest(unittest.TestCase):
    def test_fibo(self):
        self.assertFalse(fibonacci(10))
        self.assertTrue(fibonacci(13))
unittest.main()

