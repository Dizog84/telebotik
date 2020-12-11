# -*- coding: utf-8 -*-
'''
Network errors could happend so be carefull!!!
'''

import telebot
import config
import os
import time

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['test'])
def find_file_ids(message):
    global music_path
    for file in os.listdir(config.music_path):
        if file.split('.')[-1] == 'ogg':
            f = open(config.music_path + file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            # А теперь отправим вслед за файлом его file_id
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(10)


if __name__ == '__main__':
    bot.polling(none_stop=True)