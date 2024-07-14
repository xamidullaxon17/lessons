# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 17:45:44 2023

@author: hp
"""


import random
from uzwords import words

def get_word():
    """uzwordsdagi so'zlarni random qilib tanlab beradi."""
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def display(user_letters,word):
    """Foydalanuvchi kiritgan harflarni oladi va random so'zda shu kiritgan harflar bormi yo'qmi tekshiradi."""
    display_letter = ''
    for letter in word:
        if letter in user_letters.upper():
            display_letter += letter
        else:
            display_letter += '-'
    return display_letter

def play():
    word = get_word()
    # So'zdagi harflar
    word_letters = set(word)
    # Foydalanuvchi kiritgan harflar
    user_letters = ''
    print(f"Men {len(word)} xonali son o'yladim. Topa olasizmi? ")
    while len(word_letters)>0:
        print(display(user_letters,word))
        if len(user_letters)>0:
            print(f"Shu vaqtgacha kiritgan harflaringiz: {user_letters}")
            
        letter = input("Harf kiriting: ").upper()
        if letter in user_letters:
            print("Bu harfni avval kiritgansiz. Boshqa harf kiriting.")
            continue # kodni boshiga qaytadi,agar continue ishlasa.
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} harfi to'g'ri")
        else:
            print("Bunday harf yo'q.")
        user_letters += letter
    print(f"Tabriklayman! {word} so'zini {len(user_letters)} ta urunish bilan topdingiz.")
    
 