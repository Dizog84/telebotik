import os
import sqlite3
'''
import time
import telebot
import shelve
from DB import SQLighter
from random import shuffle
'''
token = ""
music_path = '/home/denis/Projects/telebotik/music/ogg/'
music_db_file = '/home/denis/Projects/telebotik/DB/music.db'



if __name__ == '__main__':
    print(os.listdir(music_path))
    db = sqlite3.connect(music_db_file)
    cur = db.cursor()
    print(type(db))
    print(type(cur))
