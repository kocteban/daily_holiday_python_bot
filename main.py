import types

import telebot
from telebot import types
import datetime


bot = telebot.TeleBot('5236914607:AAH-9RQudTWP7K5UfYwhXT2RvEK9q0fdWMg')

current_month_name = datetime.datetime.now().strftime("%B")
current_day_num = datetime.datetime.now().strftime("%d")

def send_funny_pic(message, month_name = current_month_name, day_num = current_day_num):
    with open(f'src/{month_name}/{day_num}.jpg', 'rb') as day_fpg:
        bot.send_photo(message.from_user.id, day_fpg)



@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Персикбот, какой сегодня праздник?')
    button2 = types.KeyboardButton(text='Я хочу ввести дату праздника сам')
    keyboard.row(button1, button2)
    bot.send_message(message.chat.id,
                     'Бажожда, спроси какой у меня какой сегодня праздник!',
                     reply_markup=keyboard)


@bot.message_handler(content_types='text')
def get_text_message(message):
    if message.text.lower() == 'персикбот, какой сегодня праздник?':
        send_funny_pic(message)

    elif message.text.lower() == 'я хочу ввести дату праздника сам':
        bot.send_message(message.chat.id,
                        'Введите дату в формате: "День Месяц" (числами)')

    else:
        with open(f'src/idk.jpg', 'rb') as day_fpg:
            bot.send_photo(message.from_user.id, day_fpg)




bot.polling(none_stop=True, interval=0)
