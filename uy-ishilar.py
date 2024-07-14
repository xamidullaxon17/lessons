# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 00:59:19 2023

@author: hp
"""

#kocha = input("Ko'changiz?\n>>>")
#mahalla = input("Mahallangiz?\n>>>")
#tuman = input("Tumaningiz?\n>>>")
#viloyat = input("Viloyatingiz?\n>>>")
#print(f"Sizning manzilingiz:\n{kocha.title()} ko'changiz\n{mahalla.title()} mahallangiz,\n{tuman.title()} tumaningiz,\n{viloyat.title()} viloyatingiz")


#a = int(input("Istalgan sonni kiriting:\n>>>"))
#b= a**2
#print(a, "ning kvadrati", b, "ga teng")
#c = a**3
#print(a, "ning kubi", c, "ga teng")

#yoshi = int(input("Yoshingiz nechida?\n>>>"))
#t_yili = 2023- yoshi
#print("Siz", t_yili, "da tug'ilgansiz")

#son = float(input("Birinchi sonni kiriting:"))
#son2 = float(input("Ikkinchi sonni kiriting:"))

#a2 = son - son2
#a3 = son * son2 
#a4 = son / son2
#print(son, "+", son2, "=", son+son2)
#print(son, "-", son2, "=", son-son2)
#print(son, "*", son2, "=", son*son2)
#print(son, "/", son2, "=", int(son/son2))


                          # 07 uy ishi

ismlar = ["Behzod","Jurat","Jasur","Alisher"]
print("Salom", ismlar[1], ", bugun choyxona bormi?\n",ismlar[2],",choyxonaga boramizmi?")

sonlar = [213,23.5,748_845_151,-34,52]
a = sonlar[0] + sonlar[1]
b = sonlar[3] - sonlar[2]**2
c = sonlar[-1] * sonlar[1]
print(a, "son katta", b, "sondan, ammo",c,"sondan kichik")


t_shaxslar = ["Alisher Navoiy","Amir Temur","Jaloliddin Manguberdi","Al-Buxoriy"]
z_shaxslar = ["Cristiano Ronaldo","Neymar","Ilon Mask","Bill Gates"]
print("Men tarixiy shaxslardan", t_shaxslar.pop(0), "bilan ko'rishishni istardim, zamonaviy shaxslardan esa",z_shaxslar.pop(2), "bilan ko'rishishni istardim, lekin eng ko'p", z_shaxslar.pop(0),"va",z_shaxslar.pop(0), "bilan birga futbol o'ynashni xohlardim.")

friends = []
friends.append("Akmal")
friends.append("Begzod")
friends.append("Jurat")
friends.append("Doniyor")
friends.append("Sardor")
friends.append("Sarvar")
print(friends)

friends.remove("Sardor")
friends.remove("Jurat")
print(friends)

friends.append("Xamidullaxon")
print(friends)
friends.insert(2,"Mahmud")
print(friends)
friends.insert(0, "Jasur")
print(friends)

mehmonlar = ["aa","aaa","aaaa","aaaaaa","aaaaaaa"]
mehmonlar.pop(1)
mehmonlar.append("aaaaaaaaaaa")
print("Kelgan mehmonlar" ,mehmonlar)





                         # 8-dasrs uy ishisi

davlatlar = ["Uzb","Usa","France","German","Dubai","Russia","Italy","Spain","Brazil"]
print(davlatlar)
print(len(davlatlar))
dav = sorted(davlatlar)
print(dav)
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
der = davlatlar
der.sort()
print(der)
der.sort(reverse=True)
print(der)

numbers = list(range(120,1202,2))
print(numbers)

summasi = sum(numbers)
print(summasi)

a = min(numbers)
b = max(numbers)
d = b - a 
e = summasi/2
print(d)
print(len(numbers))

#print(numbers[0:20])
#print(numbers[540:560])
#print(numbers([1180:1200]))

taomlar = ["osh","halim","norin","gumma", "sho'rva"]
print(taomlar)
nonushta = taomlar[:]
nonushta.remove("halim")
nonushta.remove("sho'rva")
nonushta.append("shashlik")
nonushta.append("chuchvara")
print(nonushta)

nonushta = tuple(nonushta)
print(nonushta)

                                # 9-dars

ismlar = ["Xamidullaxon","Behzod","Bobur","Alisher","Abdulla"]
for ism in ismlar:
    print("Salom,",ism) 
print("Kod 5 martta takrorlandi")
print("**********************************************************")

sonlar = list(range(11,101,2))
for son in sonlar:
    print(son**3)                               
print("**********************************************************")

#kinolar = []
#kino = ("5 ta eng yoqtirgan kinolaringizni kiriting!")
#print(kino)
#for k in range(5):
#    kinolar.append(input(f"{k+1}-kinoingiz "))
#print(kinolar)
 
#odamlar = []
#soni = input("Bugun nechta odam bilan ko'rishdingiz?")
#print(soni) 
#for s in range(5):
#    odamlar.append(input(f"{s+1}-insonning ismi nima?"))
#print(odamlar, "Siz bugun shu insonlar bilan ko'rishgan ekansiz!!!")    


                            # 10-dars
                    
cars = ["toyota","mazda","hyundai","gm","kia"]
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())
print("**********************************************************")

mashinalar = ["bugatti","ferarri","lamborghini","urus","audi"]
for mashina in mashinalar:
        if mashina != "urus":
            print(mashina.title())
        else: 
            print(mashina.upper())
print("**********************************************************")            
            
login = input("Login ismingizni kiriting...\n")
#for log in login:
if login.title() == "Admin":
        print(f"Xush kelibsiz, {login.title()}!")
else:
        print("Xush kelibsiz, yangi foydalanuvchi",login.title())     
print("**********************************************************")        

sonlar = ("Ikkita son kiriting>>> ")
print(sonlar)
son1 = int(input("1-son: "))
son2 = int(input("2-son: "))
if son1 == son2:
    print("Sonlar bir-biriga teng!")
else: print("Sonlar teng emas!")    
print("**********************************************************")  

son = int(input("Istalgan son kiriting!"))
if son>=0:
    print(f"{son} musbat!")
else:
    print(f"{son} manfiy!")    
print("**********************************************************")  

son1 = int(input("Son kiriting>>>"))
if son1>0:
  print(f"{son1/2}ga teng")




















                          