import json
import os
import requests
import telebot
import time
from telebot import types
from dotenv import load_dotenv
from telebot.types import BotCommand

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

RADARR_API_URL = os.getenv('RADARR_API_URL')
RADARR_API_KEY = os.getenv('RADARR_API_KEY')

command = [
    BotCommand("start", "Start"),
    BotCommand("search", "Search Movies")
]

bot.set_my_commands(command)


@bot.message_handler(commands=['start'])
def start(message):
    if check_user_auth(message.from_user.username):
        bot.send_message(message.from_user.id, '🌟 Welcome to Plexx 🌟\n\nType /search to search a Movie')
    else:
        bot.send_message(message.from_user.id,
                         '🛑 <b>Unauthorized User:</b> Contact the administrator',
                         parse_mode='HTML')


@bot.message_handler(commands=['search'])
def search_init(message):
    if check_user_auth(message.from_user.username):
        bot.send_message(message.from_user.id, 'Type the movie title:')
        bot.register_next_step_handler(message, search)
    else:
        bot.send_message(message.from_user.id,
                         '🛑 <b>Unauthorized User:</b> Contact the administrator',
                         parse_mode='HTML')


def check_user_auth(username):
    telebot_private = os.getenv('TELEBOT_PRIVATE')
    telebot_enabled_username = os.getenv('TELEBOT_ENABLED_USERNAME')

    if int(telebot_private) == 1:
        # Private Bot
        if username in telebot_enabled_username.split(' '):
            # Username Authorized
            return True
        else:
            # Username Unauthorized
            return False
    else:
        # Public Bot
        return True


def search(message):

    url = RADARR_API_URL + '/movie/lookup?term=' + message.text
    headers = {'X-Api-Key': RADARR_API_KEY}
    response = requests.get(url, headers=headers).json()

    if len(response) > 0:
        for movie_data in response:

            time.sleep(0.2)

            if movie_data['hasFile']:
                download_button = types.InlineKeyboardButton('✅ Already available on Plex', callback_data="0")
            else:
                download_button = types.InlineKeyboardButton('➕ Add to Plex', callback_data=movie_data['tmdbId'])

            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(download_button)

            if 'remotePoster' in movie_data and movie_data['year'] != 0 and movie_data['title'] != '':

                movie_info = movie_data['title'] + " (" + str(movie_data['year']) + ")"
                movie_cover = movie_data['remotePoster']

                try:
                    bot.send_message(message.from_user.id, '----------------------------------------------------')
                    bot.send_photo(message.from_user.id, str(movie_cover), caption=str('<b>' + movie_info + '</b>'),
                                   parse_mode='HTML', reply_markup=keyboard)
                except:
                    bot.send_message(message.from_user.id, str('<b>' + movie_info + '</b>'),
                                     parse_mode='HTML', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, f'🤦🏼‍No results for "{message.text}"')
        bot.register_next_step_handler(message, search)


@bot.callback_query_handler(func=lambda call: True)
def query_handler(message):
    if message.data != "0":
        url = RADARR_API_URL + '/movie/lookup/tmdb?tmdbId=' + message.data
        headers = {'X-Api-Key': RADARR_API_KEY}
        response = requests.get(url, headers=headers)

        search_response = response.json()

        search_response['qualityProfileId'] = 1
        search_response['monitored'] = True
        search_response['minimumAvailability'] = "announced"
        search_response['rootFolderPath'] = "/movies"

        search_response['addOptions'] = {}
        search_response['addOptions']['monitor'] = "movieOnly"
        search_response['addOptions']['searchForMovie'] = True

        url = RADARR_API_URL + '/movie'
        headers = {'X-Api-Key': RADARR_API_KEY, 'Content-Type': 'application/json'}

        # Add movie to Radarr
        requests.post(url, headers=headers, data=json.dumps(search_response))

        bot.answer_callback_query(message.id, '✅ ' + search_response['title'] + ' has been added to downloads',
                                  show_alert=True)


bot.infinity_polling()