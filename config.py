import os
import sqlite3
'''
import time
import telebot
import shelve
from DB import SQLighter
from random import shuffle
'''
token = "1349596380:AAHZTQxvYNelGIbNLR_c8VBr-Q3huQzE6o0"
music_path = '/home/denis/Projects/telebotik/music/ogg/'
music_db_file = '/home/denis/Projects/telebotik/DB/music.db'
music_shelve = 'home/denis/Projects/telebotik/DB/shelve.db'


if __name__ == '__main__':
    print(os.listdir(music_path))
    db = sqlite3.connect(music_db_file)
    cur = db.cursor()
    print(type(db))
    print(type(cur))
