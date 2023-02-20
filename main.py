import types

import telebot
from telebot import types
import datetime

bot = telebot.TeleBot() #insert your key

current_month_name = datetime.datetime.now().strftime("%B")
current_day_num = datetime.datetime.now().strftime("%d")


def send_funny_pic(message, month_name=current_month_name,
                   day_num=current_day_num):
    with open(f'src/{month_name}/{day_num}.jpg', 'rb') as day_fpg:
        bot.send_photo(message.from_user.id, day_fpg)


def create_date_numbers(message):
    try:
        date_num = message.text.split()[0]
        date_num = date_num.replace('0', '')
        month_num = message.text.split()[1]
        date_num = date_num.replace('0', '')
        datetime_object = datetime.datetime.strptime(month_num, "%m")
        full_month_name = datetime_object.strftime("%B")
    except:
        bot.send_message(message.chat.id, 'Извини, я тебя не понял')
    try:
        send_funny_pic(message, month_name=full_month_name, day_num=date_num)
    except:
        bot.send_message(message.chat.id,
                         'Извини, у меня пока нет картинки на такой день')


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
        send = bot.send_message(message.chat.id,
                                'Введите дату в формате: "День Месяц" (17 05 '
                                'или 05 07)')

        bot.register_next_step_handler(send, create_date_numbers)

    else:
        with open(f'src/idk.jpg', 'rb') as day_fpg:
            bot.send_photo(message.from_user.id, day_fpg)


bot.polling(none_stop=True, interval=0)
