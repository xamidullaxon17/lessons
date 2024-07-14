# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:08:34 2023

@author: hp
"""

                              #  Nesting - lug'at ichida lug'at, lu'gatning ichida list
                              
car1 = {
        "model":'gentra',
        'rangi':'qora',
        'yurgani':'4000 km',
        'yili':'2022',
        'narxi':'18000$'
        }                              
car2 = {
        "model":'lasetti',
        'rangi':'oq',
        'yurgani':'12000 km',
        'yili':'2015',
        'narxi':'14000$'
        }  
car3 = {
        "model":'cobalt',
        'rangi':'qizil',
        'yurgani':'45000 km',
        'yili':'2014',
        'narxi':'12000$'
        }  

cars = [car1,car2,car3]
for car in cars:
    print(f"{car['model'].title()}:"
          f"{car['rangi']}, "
          f"{car['yurgani']}, "
          f"{car['yili']}, "
          f"{car['narxi']}")
              
print(cars[1]['rangi'])
 
                                     # for tsikli
                                     
malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang':None,
        'yil':2020,
        'narx':None,
        'km':0,
        'korobka':'avtomat'
        }
    malibus.append(new_car)    
        
print(malibus)

for malibu in malibus[:3]:
    malibu['rang']='qizil'
    
for malibu in malibus[3:6]:
    malibu['rang']='qora'
    
for malibu in malibus[6:]:
    malibu['rang']='ko\'k'
    malibu['korobka']='mexanika'
    
for malibu in malibus:
    if malibu['korobka']=='avtomat':
        malibu['narx']=40000
    else:
        malibu['narx']=35000

for malibu in malibus:
    print(malibu)

                           # Lug'at ichida ro'yxat
                           
dasturchilar = {
    'ali':['phyton','C++'],
    'vali':['html','css','js'],
    'hasan':['php','Sql'],
    'husan':['phyton','php'],
    'maryam':['c++','c#']
    }
              
for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())
        
        # print barcha ma'lumotni alihida satrda ko'rsatadi 
        # buni bitta qatorda ko'rsatish uchun: , end=''
            
for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ", end='')
    for til in tillar:
        print(f"{til.upper()} ", end='')

hamkasblar = {
    'ali':{'familya':'valiyev',
           'yili':1995,
           'malumot':'oliy',
           'tillari':['phyton','c++']
           },
    'vali':{'familya':'aliyev',
           'yili':1995,
           'malumot':'orta-maxsus',
           'tillari':['html','css','js']
           },
    'hasan':{'familya':'husanov',
           'yili':1999,
           'malumot':'maxsus',
           'tillari':['phyton','php']}
    }

for ism,info in hamkasblar.items():
    print(f"\n{ism.title()}{info['familya'].title()}, "
          f"{info['yili']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}.\n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillari']:
        print(f"{til.upper()} " , end='')
        
 
















    
              
              