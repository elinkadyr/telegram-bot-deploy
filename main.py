import telebot
from decouple import config


token = config("TOKEN")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'hi'])
def start_message(message):
    bot.send_message(message.chat.id, "Hello")

bot.polling(none_stop=True)