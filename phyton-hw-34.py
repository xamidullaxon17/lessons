# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:03:34 2023

@author: hp
"""

#                               34 - HomeWork
import json
# 1
data = {
        'Model':'Malibu',   
        'Rang':"Qora",
        'Yil':2020,
        'Narh':40000
        }

data_json = json.dumps(data,indent=4)
print(data_json)
    
# 2
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba = json.loads(talaba_json)
print(f"talaba {talaba['ism']} {talaba['familiya']}.")

# 3
with open('dars_34.json',"w") as f:
    json.dump(data,f)
with open('dars_34_2.json',"w") as f:
    json.dump(talaba,f)

# 4
filename = 'students.json'
with open(filename) as f:
    datas = json.load(f)

for item in datas["student"]:
    print(f"{item['name']} {item['lastname']}. {item['year']}-kurs, {item['faculty']} talabasi.")

# 5
with open('api-result.json') as f:
    wiki = json.load(f)
# wikii = json.dumps(wiki,indent = 4)
# print(wikii)
print(f"{wiki['query']['pages']['13801']['title']}\n{wiki['query']['pages']['13801']['extract']}")














