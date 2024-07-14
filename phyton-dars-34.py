# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 00:29:58 2023

@author: hp
"""

#                                    34 - dars 

# import json
# import googlemaps
# from apikwy import APIKEY

# # GoogleMaps
# gmaps = googlemaps.Client(Key=APIKEY)

# data = gmaps.data('Olmazor, Tashkent, Uzbekistan')
# # print(data)

# g = json.dumps(data[0], indent = 4, sort_keys = True) # indent - chap tomondan joy tashlaydi
# print(g)

# data = data[0]
# kenglik = data['geometry',]
#
#



import json # format, ma'lumotlarni saqlash turi 

x = 10 # x ni json formatiga o'tkazish uchun
x_json = json.dumps(x) # .dumps bu str ko'rinishiga keltiradi.
# type(x) bundan int chiqadi
# print(x) bundan 10 chiqadi
# type(x_json) bundan str chiqadi
# print(x_json) bundan 10 chiqadi faqat matn ko'rinishida

y = 2.2
y_json = json.dumps(y) # bu str boladi
m = True
m_json = json.dumps(m) # bu javascript bo'gani uchun true boladi.
print(json.loads(m_json)) # bunda ro'yhatga o'tadi.

ism = 'anvar'
ism_json = json.dumps(ism)

sonlar = (12,45,23,67)
sonlar_json = json.dumps(sonlar)

print(json.loads(sonlar_json)) # .loads qaytadan pythonga o'tqazadi


bemor = {
    'ism':'Alijon Valiyev',
    'yosh':30,
    'oila': True,
    'farzandlari': ('Ahmad','Bonu'),
    'allergiya': None,
    'dorilar':[
        {'nomi':"Analgin",'miqdori':0.5},
        {'nomi':"Panadol",'miqdori':1.2}
    ]
}
#bemor_json = json.dumps(bemor)
bemor_json = json.dumps(bemor,indent=4)
print(bemor_json)
# konsolga
# bemor.keys()
# bemor['dorilar']
# bemor['nomi']
# bemor

# jsonni faylga yozish uchun
with open('bemor_json','w') as f:
    json.dump(bemor,f)

# jsonda formatida saqlangan fayllarni pythonga o'tkazish
bemor2 = json.loads(bemor_json)

# fayllarni ochish
filename = 'bemor_json'
with open(filename) as f:
    bemor = json.load(f)
    





















