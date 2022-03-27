import telebot
import timeit


bot = telebot.TeleBot('5236914607:AAH-9RQudTWP7K5UfYwhXT2RvEK9q0fdWMg')


@bot.message_handler(content_types='text')
def get_text_message(message):
    if message.text.lower() == 'персикбот, какой сегодня праздник?':
        bot.send_message(message.from_user.id, 'Такой то!')
    else:
        bot.send_message(message.from_user.id, 'Я вас не понял =(')






bot.polling(none_stop=True, interval=0)
