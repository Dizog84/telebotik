
import telebot

import config
import Utils
import keyboard

import random
from DB import SQLighter


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['game'])
def game(message):
    # Подключаемся к БД
    db_worker = SQLighter(config.music_db_file)
    # Получаем случайную строку из БД
    row = db_worker.select_single(random.randint(1, Utils.get_rows_count()))
    # Формируем разметку
    markup = keyboard.generate_markup(row[2], row[4])
    # Отправляем аудиофайл с вариантами ответа
    bot.send_voice(message.chat.id, row[1], reply_markup=markup)
    # Включаем "игровой режим"
    Utils.set_user_game(message.chat.id, row[2])
    # Отсоединяемся от БД
    db_worker.close()


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    # Если функция возвращает None -> Человек не в игре
    answer = Utils.get_answer_for_user(message.chat.id)
    # Как Вы помните, answer может быть либо текст, либо None
    # Если None:
    if not answer:
        bot.send_message(message.chat.id, 'Чтобы начать игру, выберите команду /game')
    else:
        # Уберем клавиатуру с вариантами ответа.
        keyboard_hider = telebot.types.ReplyKeyboardRemove()
        # Если ответ правильный/неправильный
        if message.text == answer:
            bot.send_message(message.chat.id, 'Верно!', reply_markup=keyboard_hider)
        else:
            bot.send_message(message.chat.id, 'Увы, Вы не угадали. Попробуйте ещё раз!', reply_markup=keyboard_hider)
        # Удаляем юзера из хранилища (игра закончена)
        Utils.finish_user_game(message.chat.id)



if __name__ == '__main__':
    Utils.count_rows()
    random.seed()
    bot.polling(none_stop=True)