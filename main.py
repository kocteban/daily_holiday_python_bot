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


def reply_to_user(message):
    bot.send_message(message.chat.id, 'Сейчас найдем!')


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text='Персикбот, какой сегодня праздник?')
    button2 = types.KeyboardButton(text='Я хочу ввести дату праздника сам')
    keyboard.row(button1, button2)
    bot.send_message(message.chat.id, 'It works!', reply_markup=keyboard)


@bot.message_handler(content_types='text')
def get_text_message(message):
    if message.text.lower() == 'персикбот, какой сегодня праздник?':
        send_funny_pic(message)


'''
    message = bot.send_message(message.chat.id,
                        'Введите дату в формате: "День Месяц" (числами)')

    try:
        bot.register_next_step_handler(message, reply_to_user)
        day_num = message.text.lower().split()[0]
        month_num = message.text.lower().split()[1]
        datetime_object = datetime.datetime.strptime(month_num, "%m")
        full_month_name = datetime_object.strftime("%B")

        send_funny_pic(message, month_name=full_month_name, day_num=day_num)

    except:
        bot.send_message(message.from_user.id, 'Я вас не понял =(')'''

    else:
        bot.send_message(message.from_user.id, 'Я вас не понял =(')


bot.polling(none_stop=True, interval=0)
