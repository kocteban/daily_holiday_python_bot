import types

import telebot
from telebot import types
import datetime


bot = telebot.TeleBot('5236914607:AAH-9RQudTWP7K5UfYwhXT2RvEK9q0fdWMg')


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Персикбот, какой сегодня праздник?')
    keyboard.row(button1)

    bot.send_message(message.chat.id, 'It works!', reply_markup=keyboard)


@bot.message_handler(content_types='text')
def get_text_message(message):
    if message.text.lower() == 'персикбот, какой сегодня праздник?':
        month_name = datetime.datetime.now().strftime("%B")
        day_num = datetime.datetime.now().strftime("%d")

        with open(f'src/{month_name}/{day_num}.jpg', 'rb') as day_fpg:
            bot.send_photo(message.from_user.id, day_fpg)

    else:
        bot.send_message(message.from_user.id, 'Я вас не понял =(')


bot.polling(none_stop=True, interval=0)
