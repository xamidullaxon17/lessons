# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 13:41:19 2023

@author: hp
                                Telegram
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = "6836200433:AAEfOD4sYoX2hOLXf20TTwrPE8QuyCP5A2g"
bot = telebot.TeleBot(TOKEN, parse_mode=None) 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalamu alaykum, Xush kelibsiz!" 
    javob += "\nMatn kiriting:"
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
     javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg) - qisqaroq varianti
    
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)


bot.infinity_polling()



















    
