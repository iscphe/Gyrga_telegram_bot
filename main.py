import telebot #библиотека бота
import requests #диагностическая информация по http запросу из бота
import cv2      #фотка с вебки
import time     #время 

#from tkinter import *#окошко
#from tkinter import messagebox

#window1 = Tk() #Создаём окно приложения.
#window1.geometry('400x300')
#window1.title("Guyrga Bot") #Добавляем название приложения.
#window1.mainloop()





############################STARTING BOT STRING###########################
token = "X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X*X"
bot = telebot.TeleBot(token)

#проверяем, есть ли коннект с серверами telegram API
var_requests = requests.get('https://api.telegram.org/bot8189940767:AAGLociI_EH-kA4TFprxirq10eI5YKx0ClI/getMe')
if var_requests.status_code == 200:
    print('Success! var_requests.status_code == 200')### показывает код 200 в консоль, что означает соединение с API установлено 

#print(var_requests, var_requests.headers) ### показывает response 200 + requests.get 

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Программа запущена. Ожидаю команду.')
    

@bot.message_handler(commands=['help'])
def main2(message):
    bot.send_message(message.chat.id, '<b>Здравствуй, уважаемый. </b> ' 
    'Меня зовут дядя Гырга. ' 
    'На сегодняшний день я уже умею делать фото с вебкамеры ' 
    'и отправлять его в чат. ' 
    'если я не отвечаю, значит я существую в форме кода, которому негде'
    ' или не зачем выполняться', parse_mode='html')

@bot.message_handler(commands=['getmessage']) #диагностика бота со стороны фронта судя по всему...
def start_message(message):
    bot.send_message(message.chat.id, var_requests.text)
    bot.send_message(message.chat.id, 'GetMe http get into tg API')

@bot.message_handler(commands=['getwebcam'])

def webfile(message):
    
    cap=cv2.VideoCapture(0) ##создаем объект для работы с камерой
    ret, frame = cap.read() #делает снимок
    print('снимок сделан')
    cv2.imwrite('cam.png',frame) #запись в файл
    print ('снимок записан в память')
    cap.release #выкл камера
    file=open('cam.png','rb')
    var_time=time.ctime() #записывает время 
    bot.send_photo(message.chat.id, file,) #отправляет фото
    bot.send_message(message.chat.id, var_time) #отправляет дату
    print ('снимок отправлен пользователю', var_time)
  


bot.infinity_polling()
