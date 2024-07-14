# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:56:41 2023

@author: hp
"""

# #                                33 - dars 

# # file = open("pi.txt")   
# # PI = file.read()
# # print(PI)
# # file.close()     # bunday ishlatish tavsiya etilmaydi


# # tafsiya etiladi:
# with open('pi.txt') as file:
#     pi = file.read()
    
# print("PI =",pi)

# pi = pi.rstrip()
# pi = pi.replace("\n",'')     
# pi = float(pi)
# print(pi)


# filename = 'data/talabalar.txt'
# # with open(filename) as file:
# #     for line in file:
# #         print(line)
        
# with open(filename) as file:
#     talabalar = file.readlines() #bu fayldagi har bir qatorni alohida element sifatida talabalar ro'yhatiga joylaydi
    
# print(talabalar)

# talabalar = [talaba.rstrip() for talaba in talabalar]
# print(talabalar)




# # faylnomi = 'new_file.txt' # agar bunday fayl bo'lsa eskisi ochib ketadi
# # ism = 'Olimjon Hasanov'
# # tyil = 2005
# # with open(faylnomi,'w') as fayl:   # w - write
# #     fayl.write(ism)
# #     fayl.write(str(tyil))

# faylnomi = "new_file.txt"
# ism = "Xamidullaxon Akromov"
# tyil = 2001
# with open(faylnomi,'w') as fayl:
#     fayl.write(ism+"\n")
#     fayl.write(str(tyil)+'\n')
     
# # faylga yangi ma'lumot qo'shamiz va bor ma'lumotlarni o'chirib tashlamaydi
# faylnomi = "new_file.txt"
# with open(faylnomi,'a') as fayl:  # a - appenddan olingan qo'shadi faylga yangi ma'lumotlarni
#     fayl.write('Alijon Valiyev\n')
#     fayl.write('2000')
 
    
 
# #                           Pickle

# import pickle 
# # pickle yordamida yozilgan fayllarni faqat pickle yordamida ko'rish mumkin. shunga pastda 'info' yoki 'info.pkl' yoki 'info.dat' deyilgan 'info.txt' emas.

# talaba1 = {'ism':'hasan','familiya':'husanov','tyil':2003,'kurs':2}
# talaba2 = {'ism':'alijon','familiya':'valiyev','tyil':2004,'kurs':1}

# with open('info','wb') as file: # wb(write binary) - ikkilik sanoq sistemasida yozish
#     pickle.dump(talaba1,file)  # dump() metodi bu
#     pickle.dump(talaba2,file)

# with open('info.dat','rb') as file:  # rb(read binary) - r - read 
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)

# print(talaba1)
# print(talaba2)

#                                       Homework
# 1 
matnnomi = "dars_33_WH.txt" 
matn = "Bugungi dars juda ham qiyinga o'xshab tuyulib ketayapti. "
matn2 = "Nafaqat bugungi balki songi 10 tacha darslarda charchab qolayapman. Negaligini tushunmayapman." 
with open(matnnomi,"w") as file:
    file.write(matn+"\n")
    file.write(matn2+"\n")

with open(matnnomi) as file:
    about = file.read()
print(about)

# 2
with open('pi_million_digits.txt','r+') as file:
    pi = file.read()
pi = pi.rstrip()
pi = pi.replace("\n",'')
pi = pi.replace(" ",'')            
# print(pi)

# 3
bday = '07022001'
print(bday in pi)

# 4 
import pickle

with open("data/new_pi.pkl",'wb') as new:
    pickle.dump(pi,new)

# with open('data/new_pi.pkl',"rb") as file:
#     pi = pickle.load(file)
# print(pi)

# 5
ism = input("Ismingiz: ").title()
familiya = input("Familiyangiz: ").title()
tyil = input("Tug'ilgan yilingiz: ")

file = 'data/new_user.txt'
with open(file,'a') as file:
    file.write(ism+' '+familiya+'\n')
    file.write(tyil+'\n')








