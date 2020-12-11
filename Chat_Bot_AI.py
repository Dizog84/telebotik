"""Бот для Телеги на Питоне pytelegrambotapi 3.5.2
почему работает кейборд вначале
"""
import config
import telebot

''' see also BotFather commands for edit Bot
 advanced wrapper for python telegramBOTAPI apiai ?
 Token on DialogFlow
 '''

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет ты написал мне \n'
    ' наверное хочешь пообщаться ?')

@bot.message_handler(content_types=['text'])
def text_(message):
    response = 'Получил Ваше сообщение :' + message.text
    bot.send_message(message.chat.id, response )



bot.polling()