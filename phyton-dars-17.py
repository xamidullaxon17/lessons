# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:47:17 2023

@author: hp
"""

                                 # 17 -dars input va while
                                 
#ism = input('Ismingiz nima? ')
#savol = f'Salom,{ism.title()}. Yoshingiz nechada? '
#yosh = input(savol)                                 
#yosh = int(yosh)
#height = input("Bo'yingiz necha metr? ")
#height = float(height)


#son = 1       # son ga 1 qiymat beramiz
#while son<=5:        # toki son 5 dan kichik yoki teng ekan...
#    print(son, end=' ')    # sonni konsolga chiqaramz
#   son += 1  # songa 1 qo'shamiz yoki son = son + 1
#('Dastur tugadi')   
    

   # while and input

#print('Kiritilgan sonning kvadratini qavtaruvchi dastur.')
#savol = "Istalgan sonni kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)
#print('Dastur tugadi')        


     # ishora
#print('Kiritilgan sonning kvadratini qavtaruvchi dastur.')
#savol = "Istalgan sonni kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
#ishora = True
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        ishora = False
#    else:    
#        print(float(qiymat)**2)
#print('Dastur tugadi')        
 

    # break while
#print('Kiritilgan sonning kvadratini qavtaruvchi dastur.')
#savol = "Istalgan sonni kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing):"
#while True:   # abadiy tsikl
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        break
#    else:
#        print(float(qiymat)**2)
#print('Dastur tugadi') 

    # break for 
#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5:
#        break
#    print(f"{son} ning kvadrati {son**2} ga teng")            

   # continue
#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5:
#        continue
#    print(f"{son} ning kvadrati {son**2} ga teng") 

    #  continue while
son = 0
while son < 10:
    son += 1
    if son%2!=0:    # % sonning juft yoki toqligini aniqlaydi bu hozir toqlarni aniqlaydi va juftlarni konsolga chiqaradi
        continue    
    else:
        print(son)
        
    # infinity loop
#soon = 0
#while soon < 10:
#    if soon%2!=0:    # % sonning juft yoki toqligini aniqlaydi bu hozir toqlarni aniqlaydi va juftlarni konsolga chiqaradi
#        continue
#    else:
#        print(soon) # bu toxtami ketvuradi       



                            # Home Work
  # 1-ish                          
kitob = "Yaxshi ko'rgan kitobingizni kiriting "
kitob += "(dasturni to'xtatish uchun 'stop' deb yozing)"
kitobi = ''
while kitobi != 'stop':
    kitobi = input(kitob)
#    if kitobi != 'stop':
#       print(f"sizning yoqtirgan kitobingiz {kitobi}.")
print("Dastur to'xtadi.")
                       
  # 2-ish
s1 = 2000
s2 = 3000
s4 = 10000
s5 = 'bepul'  
savol = ("yoshingiz nechada?")






































  