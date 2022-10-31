import os
import random
import telebot
import requests

from telebot import types
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


bot = telebot.TeleBot(os.getenv('TG_TOKEN'), parse_mode=None)

DOTERS = ['alex_yavor', 'olegya76', 'bushiqe', 'Scythe_1998']
AUDIO_DOTA = [
    'Tusk_start.mpeg',
    'Pudge_good_idea.mpeg',
    'Sniper_ho-ha.mpeg',
    'Sniper_easy_to_die.mpeg',
    'Disruptor_only_one_chance.mpeg',
    'Windranger_wind_in_back.mpeg',
    'Gyro_attack_04_ru.mp3.mpeg',
    'Gyro_attack_18_ru.mp3.mpeg',
    'Gyro_call_down_02_ru.mp3.mpeg',
    'Gyro_kill_16_ru.mp3.mpeg',
    'Zuus_haste_02_ru.mp3.mpeg',
    'Wdoc_spawn_04_ru.mp3.mpeg',
    'Wdoc_attack_02_ru.mp3.mpeg',
    'Wdoc_rare_04_ru.mp3.mpeg',
    'Jug_acknow_05_ru.mp3.mpeg',
    'Jugg_rival_01_ru.mp3.mpeg',
    'Jug_bottle_03_ru.mp3.mpeg',
    'Jug_rare_05_ru.mp3.mpeg',
    'Drag_inthebag_01_ru.mp3.mpeg',
    'Bristle_death_02_ru.mp3.mpeg',
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здарова, ёпта')


@bot.message_handler(commands=['dota'])
def invite_doters(message):
    DOTERS.remove(message.from_user.username)
    if len(DOTERS) == 2:
        file = open(f'audio/{random.choice(AUDIO_DOTA)}', 'rb')
        bot.send_audio(message.chat.id, file, caption=f'Го в доту @{DOTERS[0]} @{DOTERS[1]}')
    else:
        bot.send_message(message.chat.id, f'Го в доту @{DOTERS[0]} @{DOTERS[1]} @{DOTERS[2]}')
    DOTERS.append(message.from_user.username)
    
@bot.message_handler(commands=['phrase'])
def random_phrase(message):
    file = open(f'audio/{random.choice(AUDIO_DOTA)}', 'rb')
    bot.send_audio(message.chat.id, file)
    

bot.infinity_polling()
