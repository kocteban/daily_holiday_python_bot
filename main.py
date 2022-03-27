import telebot
import timeit


bot = telebot.TeleBot('5236914607:AAH-9RQudTWP7K5UfYwhXT2RvEK9q0fdWMg')


@bot.message_handlers(content_types=['text'])
def get_text_message(message):
    if message == 'Какой сегодня праздник?':
        bot.send_message()
