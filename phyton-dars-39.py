# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 14:04:43 2023

@author: hp
"""

#                                       39 - dars

#                                     1
"""googletrans - Ushbu modul yordamida Googlening tarjimonlik xizmatiga murojat qilib, 
istalgan matnni turli tillarga tarjima qilishimiz mumkin"""
# from googletrans import Translator
# tarjimon = Translator()
# matn_uz = "Phyton - dunyodagi eng mashhur dasturlash tili"

# # matnni ing tiliga o'girish
# tarjima = tarjimon.translate(matn_uz)
# # original matn
# print(tarjima.origin)
# # tarjima
# print(tarjima.text)
# # original matn tili
# print(tarjima.src)


# # boshqa tilga tarjima qilish uchun dest parametridan foydalanamiz
# tarjima_ru = tarjimon.translate(matn_uz,des='ru')
# print(tarjima_ru.text)

# # ing tilidan tarjima
# matn_en = "Tashkent is the capital of Uzbekistan"
# print(matn_uz)


# msg = "Tarjima uchun so'z kiriting (chiqib ketish uchun 'q' deb yozing): "
# while True:
#     text = input(msg)
#     if text == "q":
#         break
#     else:
#         tarjima = tarjimon.tranlate(text,src='uz',dest='en')
#         print(tarjima.text)




#                                           2
"""requests - Bu paket yordamida Pythonda veb sahifalarga murojat qilishimiz (so'rov yuborishimiz) va ulardan qaytgan ma'lumotlar ustida turli amallar bajarishimiz mumkin. """
# import requests  # internetdagi sahifalarni chaqirib oladi
# from pprint import pprint

# # sahifa = 'https://kun.uz/news/main'
# # r = requests.get(sahifa)
# # pprint(r.text)

# # restcountries API # API - onlinedagi tayyor xizmatlar bor. va ularga murojaat qilish 
# country = "Uzbekistan"
# url = f"https://restcountries.eu/rest/v2/name/{country}"
# r = requests.get(url)
# r_json = r.json()[0]
# print(r.json.keys())
# print(r_json['capital'])
# print(r_json)




#                                            3 
# import requests
# import googletrans

# url = "hhtps://api.afviceslip/com/advice"
# r = requests.get(url)
# advice = r.json()['slip']['advice']
# print(advice)

# translator = googletrans.Translator()
# tarjima = translator.translate(advice,dest = 'uz')
# print(tarjima.text)


#                                             4
"""BeautifulSoup juda kuchli modullardan biri bo'lib, bu modul yordamida turli veb sahifalardan 
istalgan ma'lumotlarni yig'ishtirib (scarpping) olish mumkin. Biror kishining instagram sahifasidagi 
barcha rasmlar deysizmi, Facebook guruhidagi barcha postlar va izohlar deysizmi, oldi-sotdi bozoridagi 
e'lonlar deysizmi, marhamat, bs4 moduli yordamida buni bemalol avtomatlashtirish mumkin. """
# from pprint import pprint
# import requests
# from bs4 import BeautifulSoup  # veb sahifadan o'zimizga kerak bo'lgan ma'lumotlarni sug'urib olishimiz mumkin.

# sahifa = 'https://kun.uz/news/main'
# r = requests.get(sahifa)
# pprint(r.text)

# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# news = soup.find_all(class_='news-title')
# print(news[0].text)


#                                              5
"""Wordcloud moduli yordamida katta matnlarda eng ko'p uchraydigan so'zlarni 
chiroyli qilib, so'zlar buluti chiqarish mumkin"""
# import requests
# from bs4 import BeautifulSoup
# from wordcloud import WordCloud 
# import matplotlib.pyplot as plt 


# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)

# soup = BeautifulSoup(r.text, 'html.parser')
# news = soup.find_all(class_="news-title")
# matn=""
# for n in news:
#     matn += n.text

# # kerakmas so'zlar
# stopwords = ["учун","бўйича","лекин","билан","ва","бор","ҳам","хил","йил"]
# # bulutni yaratamiz
# wordcloud = WordCloud(width = 1000, height = 1000, 
#                 background_color ='white', 
#                 stopwords = stopwords, 
#                 min_font_size = 20).generate(matn) 
  
# # plot the WordCloud image                        
# plt.figure(figsize = (8, 8), facecolor = None) 
# plt.imshow(wordcloud) 
# plt.axis("off") 
# plt.tight_layout(pad = 0) 
# plt.show() 


#                                           6
"""fuzzywuzzy - Bu modul yordamida so'zlarni bir-biriga solishtirish yoki matnlar tarkibida 
kerakli so'zni topishda foydalanamiz. """
# from fuzzywuzzy import fuzz
# print(fuzz.ratio("salom",'assalom'))
# print(fuzz.ratio("salom","salim"))

# # Matnlar orasidan eng o'xshashini topish
# text = "талба"
# match = process.extractOne(text,words)
# print(match)





#                                           7
"""wxPython paketi deyarli barcha operatsion tizimlarda ishlaydigan grafik interfeysli dasturlar 
yaratish uchun mo'ljallangan. Bu paket haqida alohida darsliklar qilish mumkin, shuning uchun biz 
faqatgina bitta misol bilan chegralanamiz."""
# import wx                       
# from googletrans import Translator

# tarjimon = Translator()
# class MyFrame(wx.Frame):    
#     def __init__(self):
#         super().__init__(parent=None, title='Oʻzbek-Ingliz Lugʻat')
#         panel = wx.Panel(self)        
#         my_sizer = wx.BoxSizer(wx.VERTICAL)        
#         self.text_ctrl = wx.TextCtrl(panel)
#         my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)        
        
#         my_btn = wx.Button(panel, label='TARJIMA')
#         my_btn.Bind(wx.EVT_BUTTON, self.on_press)
#         my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        
#         self.text_out = wx.TextCtrl(panel,style = wx.TE_READONLY)        
#         my_sizer.Add(self.text_out, 0, wx.ALL | wx.EXPAND, 5)         
#         panel.SetSizer(my_sizer)        
#         self.Show()

#     def on_press(self, event):
#         value = self.text_ctrl.GetValue()
#         if not value:                       
#             self.text_out.SetValue("Soʻz kiritmadingiz")
#         else:
#             tarjima = tarjimon.translate(value, src='uz', dest='en')
#             self.text_out.SetValue(tarjima.text.capitalize()) 
    

# if __name__ == '__main__':
#     app = wx.App()
#     frame = MyFrame()
#     app.MainLoop()





#                                           8
"""openCV bu kompyuter yordamida rasm va video tasvirlar bilan ishlash uchun maxsus kutubxona. 
Bugungi kunda sun'iy intellekt yordamida tasvirlar bilan ishlaydigan dasturlarning deyarli barchasi 
openCV yordamida yaratiladi. 
Bu dastur yordamida rasm va videolardagi turli obyektlarni "ko'rish", ajratib olish mumkin. 
Avtomobillar nomerini aniqlash, odamlarning yuzidan tanish, obyektlarni klassifikasiya qilish kabi 
dasturlarning kasari aynan openCV kutubxonasi yordamida ishlaydi."""
# import cv2

# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# while True:
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
#         roi_gray = gray[y:y+w, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]
#         eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
#         for (ex, ey, ew, eh) in eyes:
#             cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

#     cv2.imshow('frame', frame)

#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# # copyright Tim Ruscia aka techwithtim
# # code from https://github.com/techwithtim/OpenCV-Tutorials




