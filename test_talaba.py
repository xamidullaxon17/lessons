# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 23:31:12 2023

@author: hp
"""

# test  

import unittest
from talaba_test import Shaxs 

class ShaxsTest(unittest.TestCase):
     def setUp(self):
        ism = "Xamidullaxon"
        familiya = "Akromov"
        passport = "AB6111499"
        tyil = 2001
        self.shaxs1 = Shaxs(ism,familiya,passport,tyil)
        
     def test_create(self):
        self.assertIsNotNone(self.shaxs1.ism)
        self.assertIsNotNone(self.shaxs1.familiya)
        self.assertIsNotNone(self.shaxs1.passport)
        self.assertIsNotNone(self.shaxs1.tyil)
        self.assertEqual(22,self.shaxs1.get_age(2023))
     
    
unittest.main()


















