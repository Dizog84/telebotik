"""Бот для Телеги на Питоне pytelegrambotapi 3.5.2
почему работает кейборд вначале
"""
import config
import telebot
''' see also BotFather commands for edit Bot '''

bot = telebot.TeleBot(config.token)


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Hi','Bye','не надо')
keyboard1.add('Hi','Bye','не надо')

@bot.message_handler(commands=["start"])      # decorator с параметром
def start_message(message):                   # message это то что присылает BOT (по факту мое исходящее!)
    print(message)


@bot.message_handler(content_types=['text'])     # decorator с параметром
def start_message(message):                       # message это то что присылает Сервер!
    bot.send_message(message.chat.id,'Привет , ты написал мне' ,reply_markup=keyboard1 )
    print(message)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'скажи мне кто я':                              #whoami
        bot.send_message(message.chat.id, str(message.from_user.first_name))
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMoX2C6YZdUtLNKS81gbs8ozI7PagwAAmYJAAJ5XOIJnwqK-WG2GEQbBA')
    else:
        bot.send_message(message.chat.id, 'что-то тут не то')
    print(message)


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)



bot.polling()

