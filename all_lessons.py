# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 00:32:33 2024

@author: hp
"""

# mevalar = ["olma","anor"]
# mevalar.append("uzum")
# mevalar.insert(1, "banan")
# print(mevalar)
# del mevalar[0]
# mevalar.insert(0, "olma")

# mevalar.remove('anor')
# print(mevalar)

# telefonlar = ["redmi","apple",'samsung','xiaomi','artel','pixel','google']
# telefon = telefonlar.pop(3)
# print(f"Men bozordan {telefon} sotib oldim")
# telefonlar.remove('pixel')
# print(telefonlar)


# # 8

# cars = ['bmw','audi','lexus','mers','bugatti','lamborghini' ]

# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)
# print(sorted(cars,reverse=True))
# print(sorted(cars))
# print(cars[0:4])
# a = len(cars)
# print(a)

# son = list(range(0,12))

# print(son)


# son = list(range(0,12,2))
# print(son)

# maks = max(son)
# mini = min(son)

# print(maks)
# print(mini)

# jami=sum(son)
# print(jami)


# print("22 ni 4 ga bo'lganda qancha qoldiq", 22%4)

# kocha=input("Ko'changiz:\n").title()

# mahalla=input("Mahallangiz:\n").title()

# tuman=input("Tumaningiz:\n").title()

# viloyat=input("Viloyatingiz:\n").capitalize()

# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")


# son_1 = int(input("Istalgan son kiriting:\n>>> "))
# print(f"{son_1} ning kvadrati {son_1**2} ga teng\n"
#       f"{son_1} ning kubi {son_1**3} ga teng")


# t_yil = int(input("yoshingizni kiriting: "))
# print(f"Siz {2024-t_yil} yilda tug'ilgansiz")

# print("Istalgan ikkita son kiriting")
# son = float(input("Birinchi son: "))
# son2 = float(input("Ikkinchi son: "))
# print(f"{son}+{son2}={son+son2}\n"
#       f"{son}+{son2}={son-son2}\n"
#       f"{son}+{son2}={son*son2}\n"
#       f"{son}+{son2}={son/son2}\n")

# ismlar = ["MUHAMMAD", "behzod", "Komila"]
# print(f"Salom,{ismlar[0].title()} bugun dars qilamizmi?\n"
#       f"Salom,{ismlar[1].capitalize()} qachon ko'rishamiz?\n"
#       f"Salom,{ismlar[2].upper()} uzur sizni tanimadim. Kimsiz?")

# sonlar = [234,543,6536,765,7856,34,234,64,67,98765,342]
# # son = float(input("1-sonni kiriting: "))
# # sonlar.append(son)
# print(sonlar)
# print(sonlar[2]+sonlar[0])
# print(sonlar[-6]-sonlar[5])
# print(sonlar[2]*sonlar[7])
# print(sonlar[4]//sonlar[4])
# del sonlar[3]
# sonlar.remove(543)
# sonlar.insert(0,123456789)
# print(sonlar.pop(6))
# print(sonlar)

# t_shaxslar = ["Amir Temur", "Alisher Navoiy", "Zahiriddin Muhammad Bobur"]
# z_shaxslar = ["Ilon Musk","Selena Gomez","Kendall Jenner","Cristiano Ronaldo"]
# print("men tarixiy shaxslardan", t_shaxslar[1] ,"bilan ko'rishishni istar edim."
#       "Zamonaviy shaxslardan esa", z_shaxslar[1],"bilan")

# mehmonlar = []
# mehmonlar.append("Alisher")
# mehmonlar.append("Selena Gomez")
# mehmonlar.append(z_shaxslar[2])
# mehmonlar.append(z_shaxslar[0])
# print(mehmonlar)
# mehmonlar.remove(mehmonlar[3])
# mehmonlar.insert(1, "Taylor Swift")

# print(mehmonlar)

# davlatlar = ["O'zbekiston","Qozog'iston", "Rossiya", "Malayziya", "Singapur", "AQSh"]
# print(davlatlar)
# print("Men kiritgan davlatlar soni: ",len(davlatlar),"ta")
# print(sorted(davlatlar))      # listga teymasdan alifbo bo'yicha qo'yish
# print(sorted(davlatlar, reverse=True))    # listga teymasdan alifboga teskari qo'yish
# print(davlatlar)
# davlatlar.reverse()      # listni o'rnini aylantirish
# print(davlatlar)
# davlatlar.sort()        # list alifbo bo'yicha qo'yiladi va list o'zgaradi
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

# sonlar = list(range(120,1200,2))
# print(sonlar)
# print(sum(sonlar))
# print(max(sonlar)-min(sonlar))
# print(len(sonlar))

# print(sonlar[:20])
# print(sonlar[260:280])
# print(sonlar[-20:])

# taomlar = ['osh','somsa','norin','shashlik','qozonkabob']
# nonushta = taomlar[:]
# nonushta.remove("osh")
# nonushta.remove("qozonkabob")
# nonushta.append('bulochka')
# nonushta.append("sosiska")
# print(taomlar)
# print(nonushta)
# nonushta = tuple(nonushta)
# print(nonushta)

# ismlar = ["Selena","Komila","Kendall","Margo","Angelina"]
# for ism in ismlar:
#     print(ism)
# print(f"Kod {len(ismlar)} marotaba qaytarildi")

# sonlar = list(range(11,100,2))
# for son in sonlar:
#     print(son**3)


# kinolar = []
# print("5 ta eng sevimli kinolaringiz qaysi?")
# for n in range(5):
#     kinolar.append(input(f"{n+1}-kinoni kiriting: "))
# print(kinolar)



# savol = int(input("Bugun nechta inson bilan ko'rishdingiz? "))
# insonlar = []
# for s in range(savol):
#     insonlar.append(input(f"{s+1}- insoningiz kim edi?"))
# print(insonlar)





# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != "gm":
#         print(car.title())
#     else:
#         print(car.upper())
        
        
# user = input("Ismingiz nima? ")
# if user.title() == "Admin":
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print("Xush kelibsiz,",user)
        
# print("Ikkita son kiriting.")
# son1 = float(input("birinchi son: "))
# son2 = float(input("ikkinchi son: "))
# if son1 != son2:
#     print("Sonlar bir-biriga teng emas.")
# else:
#     print("Sonlar bir-biriga teng")

# son = int(input("Istalgan son kiriting: "))
# if son>=0:
#     print(f"{son} Musbat son")
# else:
#     print(f"{son} manfiy son")

# son = float(input("Istalgan son kiriting: "))
# print(son**(1/2)) if son>0 else print("Musbat son kiriting.")




# son = int(input("Juft son kiriting: "))
# if son % 2:
#     print(f"{son} bu juft son emas")
# else:
#     print("Rahmat")


# yosh = int(input("Yoshingizni kiriting: "))

# if yosh<=4 or yosh>=60:
#     narx = 0
# elif yosh<=18:
#     narx = 10000
# elif yosh > 18:
#     narx = 20000
# print(f"Sizga kirish {narx} so'm")

# son1 = float(input("Birinchi son: "))
# son2 = float(input("Ikkinchi son: "))
# if son1>son2:
#     print(f"{son1}>{son2}")
# elif son1<son2:
#     print(f"{son1}<{son2}")
# else:
#     print(f"{son1} = {son2}")


# mahsulotlar = ['olma','anor','uzum','behi','gilos','banan','shaftoli','nok','anjir','xurmo']
# savat = []

# print("5 ta maxsulot kiriting: ")
# for n in list(range(1,6)):
#     a = input(f"{n}-maxsulotni qo'shing: ")
#     savat.append(a)
# print(savat)   
# for mahsulot in savat:    
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")

# mahsulotlar = ['olma','anor','uzum','behi','gilos','banan','shaftoli','nok','anjir','xurmo']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []

# print("5 ta maxsulot kiriting: ")
# for n in list(range(1,6)):
#     a = input(f"{n}-maxsulotni qo'shing: ")
#     savat.append(a)
# print(savat)   
# for mahsulot in savat:    
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
        
# if mavjud_emas:
#     print("Quyidagi mahsulotlar do'konimizda yo'q:")
#     for yoq in mavjud_emas:
#         print(yoq)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")



# foydalanuvchilar = ["user1","user2","user3","user4","user5"]
# login = input("Yangi login kiriting: ")
# if login.lower() in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {login}")


# son = int(input("Butun son kiriting: "))

# for w in list(range(2,11)):
#     if not (son%w) :
#         print(f"{son} soni {w} ga qoldiqsiz bo'linadi.")

    

# car_0 = {'model':'ferarri','rang':'qizil'}
# print(car_0['model'])    
# print(car_0['rang'])    

# en_uz = {'apple':"olma","apricot":"o'rik","banana":"banan"}
# print(en_uz['apple'])  


# en_uz["grass"] = "o't"

# print(en_uz)  

# telefonlar = {
#     "zohid":"samsung",
#     "davron":"pixel",
#     "bobur":"apple",
#     "xami":"redmi"
#         }
# phone = telefonlar.get("xasan","Bunday ism mavjud emas! ") # agar ism bolsa hasandagi telefon chiqadi , agar bo'lmasa,"Bunday ism mavjud emas! " chiqDI 
# print(phone)

# ota = {"ism":"Bobur",
#        "familiya":"Akromov",
#        "t_yil":1962}

# print(f"Otamning ismi {ota['ism'].title()}."
#       f"Familiyasi {ota['familiya'].title()}."
#       f"Tug'ilgan yillari {ota['t_yil']}")


# ota = {"Bobur":"osh",
#        "Xamidullaxon":"norin",
#        "Abdulla":"lag'mon"}

# print(f"Boburning yoqtirgan taomi {ota['Bobur']}")
# print(f"Xamidullaxon yoqtirgan taomi {ota['Xamidullaxon']}")
# print(f"Abdullaning yoqtirgan taomi {ota['Abdulla']}")


# kalit = {"if":"agar",
#          "else":"boshqa",
#          "or":"yoki",
#          "not":"yoq"
#          }

# # soz = input("Biror bir so'z kiriting: ").lower()
# # a = kalit.get(soz,"Bunday so'z mavjud emas.")
# # print(a)


# soz = input("Kalit so'z kiriting:").lower()
# tarjima = kalit.get(soz)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{soz.title()} so'zi {tarjima} deb tarjima qilinadi")
    




# lugat = {"if":"agar",
#          "or":"yoki",
#          "and":"va",
#          "else":"boshqa",
#          "input":"so'rash",
#          "while":"toki",
#          "for":"uchun",
#          "in":"da",
#          "tuple":"o'zgarmas",
#          "list":"ro'yxat"}

# for key, value in sorted(lugat.items()):
#     print(f"{key} so'zining ma'nisi - {value}")




# davlatlar = {"USA":"New-York",
#              "France":"Parig",
#              "Spain":"Madrid",
#              "UK":"England",
#              "Russia":"Moskva",
#              "Italy":"Roma"}

# # for davlat in sorted(davlatlar.keys()):
# #     print(davlat)
# # for davlat in sorted(davlatlar.values()):
# #     print(davlat)
 
# country = input("Istalgan davlat kiring: ")
# capital = davlatlar.get(country)
# if capital == None: 
#     print("Mavjud emas")
# else:
#     print(f"{country}ning poytaxti - {capital}")    # capital qattan keganini o'rganish kere


# taomlar = {"osh":20000,
#           "norin":14000,
#           "sho'rva": 5000,
#           "joxori":4000,
#           "makaron":5000,
#           "manti":11000,
#           "lag'mon":10000,
#           "somsa":6000,
#           "beshbarmoq":20000,
#           "shashlik":25000}

# print("3 ta taom buyurtma bering:")
# royxat = []
# for n in list(range(1,4)):
#     royxat.append(input(f"{n} - taom: ").lower()) 
# for taom in royxat:
#     if taom in taomlar:
#         print(f"{taom} {taomlar[taom]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {taom} yo'q.")




# ism1 = {"Alisher Navoiy 1441-yilda Hirot shaxrida tug'ilgan. yoshligidan she'r, adabiyotga qiziqishi yuqilri bo'lgan"}

# ism2 = {"Ilon Musk dunyoning eng boy insoni. Uning hisobida 180_000_000_000 dollar puli bor."}

# ism3 = {"Cristiano Ronaldo dunyoning eng mashxur futbolchisi. U dunyoning eng zo'r futbolchisi deb tan olingan."}

# ism = [ism1,ism2,ism3]

# for i in ism:
#     print(i)
# print(ism[0])


# adabiyot1 = {"ism":"Alisher Navoiy",
#             "t_yil":1441,
#             "asarlari":["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub"],
#             "malumot":"Alisher Navoiy 1441-yilda Hirot shaxrida tug'ilgan. yoshligidan she'r, adabiyotga qiziqishi yuqilri bo'lgan"}
# adabiyot2 = {"ism":"Ilon Musk",
#             "t_yil":1982,
#             "asarlari":["Tesla","Space X","X"],
#             "malumot":"Ilon Musk dunyoning eng boy insoni. Uning hisobida 180_000_000_000 dollar puli bor."}
# adabiyot3 = {"ism":"Alisher Navoiy",
#             "t_yil":1985,
#             "asarlari":["Oltin to'p","Mr-Champions league","G.O.A.T"],
#             "malumot":"Cristiano Ronaldo dunyoning eng mashxur futbolchisi. U dunyoning eng zo'r futbolchisi deb tan olingan."}

# adabiyot = [adabiyot1,adabiyot2,adabiyot3]

# for adab in adabiyot:
#     ism = adab["ism"]
#     asarlar = adab["asarlari"]
#     print(f"\n{adab['ism']}ning mashhur ishlari: ")
#     for asr in asarlar:
#         print(asr)

# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }

# for key, value in kinolar.items():
#     print(f"{key}ning sevimli kinolari: ")
#     for k in value:
#         print(k)
        

# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# for davlat, info in davlatlar.items():
#     print(f"{davlat.title()}ning poytaxti {info['poytaxt']}\n"
#           f"Hududi: {info['maydon']}\n"
#           f"Aholi: {info['aholi']}\n"
#           f"Pul birligi: {info['pul birligi']}")

# savol = input("Davlat nomini kiriting: ")

# if savol in davlatlar:
#     info = davlatlar[savol]
#     print(f"\n{savol.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#     f"\nHududi: {info['maydon']} kv.km"
#     f"\nAholisi: {info['aholi']}"
#     f"\nPul birligi: {info['pul birligi']}")
# else:
#     print(f"Bizda {savol.title()} haqida ma'lumot mavjud emas.")





# savol = "Yoqtirgan futbolchilaringizni kiriting: "
# savol += ("(Dasturni toxtatish uchun 'stop' deb yozing.)\n>>> ")
# kitoblar = []
# while True:
#     kitob = input(savol)
#     if kitob == "stop":
#         break
#     else:
#         kitoblar.append(kitob)

# print(kitoblar)


# savol = ("Yoshingizni kiriting: ")
# savol += ("Chiqish uchun 'stop' yoki 'quit' tugmasini bosing.\n")


# while True:
#     yosh = input(savol)
#     if yosh == 'stop' or yosh == 'quit':
#         break
#     yosh = int(yosh)

#     if yosh < 7:
#         narx = 2000
#     elif 18 > yosh >= 7:
#         narx = 3000
#     elif 18 <= yosh < 65:
#         narx = 10000
#     else: narx = 0

#     if narx == 0:
#         print("Sizga kirish be'pul")
#     else:
#         print(f"Sizga kirish {narx} so'm")



# mahsulotlar = []

# while True:
#     savol = input("Mahsulotlarni kiriting: ")
#     if savol == 'quit':
#         break
#     else:
#         mahsulotlar.append(savol)
# print("Siz quyidagi mahsulotlarni kiritdingiz:")
# for mahsulot in mahsulotlar:
#     print(mahsulot, end = ' ')



# e_bozor = {}
# while True:
#     savol = input("Mahsulot nomini kiriting: ")
#     if savol != 'stop':
#         narx = int(input("Maxsulot narxini kiriting: "))
#         e_bozor[savol] = narx
#     else:
#         break
# for bozor, narh in e_bozor.items():
#     print(f"{bozor}ning narxi {narh}")

# # similar
# e_bozor = {}
# while True:
#     savol = input("Mahsulot nomini kiriting: ")
#     if savol == 'stop':
#         break
#     narx = int(input("Maxsulot narxini kiriting: "))
#     e_bozor[savol] = narx
# for bozor, narh in e_bozor.items():
#     print(f"{bozor.title()}ning narxi {narh}")


# mahsulotlar = ["olma",'anor','behi','kiwi','uzum']
# e_bozor = {"olma":24000,"banan":30000,"kiwi":50000,"nok":45000,}
# while mahsulotlar:
#     mahsulot = mahsulotlar.pop()
#     if mahsulot in e_bozor.keys():
#         narh = e_bozor[mahsulot]
#         print(f"{mahsulot} narxi {narh} so'm.")
#     else:
#         print(f"Bizda {mahsulot} yo'q.")



# def sora(ism,yosh):
#     print(f"{ism.title()} siz {2024-yosh} yoshda ekansiz.")
# sora("Xamidullaxon",2001)

# def son_kirit(son):
#     print(f"{son} ning kvadrati: {son**2}")
#     print(f"{son} ning kubi: {son**3}")
# son_kirit(3)

# def son_ber(son):
#     if son % 2 == 0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")
# son_ber()

# def sonlar(a,b):
#     if a > b:
#         print(f"{a} > {b} ")
#     elif a < b:
#         print(f"{a} < {b} ")
#     else:
#         print("Sonlar bir-biriga teng")
# sonlar(3,3)

# def son_kere(a,b):
#     print(a**b)
# son_kere(3,5)

# def son_kere(a,b=2):
#     print(a**b)
# son_kere(10)

# def son_qabul(x):
#     for y in list(range(2,11)):
#         if x % y == 0:
#             print(f"{x} {y} ga qoldiqsiz bo'linadi.")
# son_qabul(2430)
    
    
        
# def son_kv(s1,s2,s3=''):
#     sonlar = []
#     while s1<s2:
#         sonlar.append(s1)
#         if s3:
#             s1 += s3
#         else:
#             s1+=1
#     return sonlar
# print(son_kv(10,20,2))
     
# def son_kv(s1,s2,s3=2):
#     sonlar = []
#     while s1<s2:
#         sonlar.append(s1)
#         s1+=s3
#     return sonlar
# print(son_kv(10,20))


# def malumot(ism, familiya, t_yil, t_joy, email = '', telefon = ''):
#     malumotlar = {"ismi":ism,
#                   "familiyasi":familiya,
#                   "tugilgan yili": t_yil,
#                   "tugilgan joyi":t_joy,
#                   "emaili": email,
#                   "telefon raqami": telefon,
#                   "yoshi":2024-int(t_yil)}
#     return malumotlar
# print(malumot("Xamidullaxon",'Akromov',2001,"o'zbekiston","xamidullaxonakromov@gmail.com"))
# print("Mijozlar haqida ma'lumot")
# mijozlar = []
# while True:
#     ism = input("Ismi: ")    
#     familiya = input("Familiyasi: ")
#     t_yil = input("Tug'ilgan yili: ")
#     t_joy = input("Tug'ilgan joyi: ")
#     email = input("Emaili: ")
#     telefon = input("Telefon raqami: ")
#     mijozlar.append(malumot(ism,familiya,t_yil,t_joy,email,telefon))
#     a = input("Yana ma'lumot qo'shasizmi? (yes/no) ").lower()
#     if a == 'no':
#         break
# print("Mijozlar: ")
# for mijoz in mijozlar:
#     print(f"Mijozning ismi: {mijoz['ismi'].title()}, "
#           f"Mijozning familiyasi: {mijoz['familiyasi'].title()}, "
#           f"Tug'ilgan yili: {mijoz['tugilgan yili']}, "
#           f"Tug'ilgan joyi: {mijoz['tugilgan joyi'].title()}, "
#           f"Email raqami: {mijoz['emaili']}.")

# def sonlar(x,y,z):
#     if x>y and x>z:
#         return x
#     elif y>x and y>z:
#         return y
#     else:
#         return z
# print(sonlar(3, 10, 7))        

# def kattasi(x, y, z):
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z
#     return max
# print(sonlar(12, 10, 87))        

# def math(r): 
#     PI = 3.14
#     malumotlar = {"radius":r,
#                   "perimetri":2*r*PI,
#                   "diametri":r*2,
#                   "yuzi":r*PI**2}
#     return malumotlar
# print(math(10))


                                                                                # def tub_sonlar_top(min, max):
                                                                                #     tub_sonlar = []
                                                                                #     for n in range(min, max + 1):
                                                                                #         tub = True
                                                                                #         if n == 1:
                                                                                #             tub = False
                                                                                #         elif n == 2:
                                                                                #             tub = True
                                                                                #         else:
                                                                                #             for x in range(2, n):
                                                                                #                 if n % x == 0:
                                                                                #                     tub = False
                                                                                #         if tub:
                                                                                #             tub_sonlar.append(n)
                                                                                #     return tub_sonlar
                                                                                # print(tub_sonlar_top(3,15))   

# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar
# print(fibonacci(50))

# def son():
#     sonlar = []
#     for x in range(1,101):
#         if x%3==0 and x%5==0:
#             sonlar.append("FizzBuzz") 
#         elif x%3==0:
#             sonlar.append("Fizz") 
#         elif x%5==0:
#             sonlar.append("Buzz") 
#         else:
#             sonlar.append(x)
#     return sonlar
# print(son())

# matn= "Rahmat Alisher aka"

# teskari_matn = matn[::-1]
# print(teskari_matn)


# def faktorial_hisobla(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         faktorial = 1
#         for i in range(2, n + 1):
#             faktorial *= i
#         return faktorial
# n = 100
# natija = faktorial_hisobla(n)
# print(f"{n} faktoriali = {natija}")



# def katta_harflar(ism):
#     ismlar = []
#     for i in ism:
#         ismlar.append(i.title())
#     return ismlar
# ism = ['ali', 'vali', 'hasan', 'husan']
# a = katta_harflar(ism)
# print(a)
# print(ism)


# def bahola(ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = baho
#     return baholar
# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(baholar)

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism]=baho
#     return baholar

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(baholar)
