import os

import requests
from loguru import logger
from telebot import types
import telebot
from dotenv import load_dotenv


load_dotenv()
FORM_URL = os.environ.get('FORM_ADS', '')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '5265303223:AAHn68aqrQaw9zThfUXFBQMX5hmgjqoTts')
HOST_URL = os.environ.get('HOST_URL', 'http://127.0.0.1:8000/')
bot = telebot.TeleBot(BOT_TOKEN)


def send_users_data(tlg_update):
    """
    Отправка данных о пользователе по API для записи в БД.
    """
    params = {
        'tlg_id': tlg_update.from_user.id,
        'is_premium': tlg_update.from_user.is_premium,
        'first_name': tlg_update.from_user.first_name,
        'last_name': tlg_update.from_user.last_name,
        'username': tlg_update.from_user.username,
        'language_code': tlg_update.from_user.language_code,
    }
    response = requests.post(f"{HOST_URL}users_data/", data=params)
    if response.status_code == 200:
        logger.success(f'Успешная запись данных о пользователе')
    else:
        logger.warning(f'Запись данных о пользователе не удалась!')


def web_app_keyboard_inline():  # создание inline-клавиатуры с webapp кнопкой
    keyboard = types.InlineKeyboardMarkup(row_width=1)  # создаем клавиатуру inline
    web_app = types.WebAppInfo(FORM_URL)  # создаем webappinfo - формат хранения url
    one = types.InlineKeyboardButton(text="🏎Наши услуги", web_app=web_app)  # создаем кнопку типа webapp
    keyboard.add(one)  # добавляем кнопку в клавиатуру
    return keyboard  # возвращаем клавиатуру


@bot.message_handler(commands=['start'])  # обрабатываем команду старт
def start_fun(message):
    bot.send_message(message.chat.id,
                     '🤝Здравствуйте.\nЧтобы ознакомиться с нашими услугами, нажмите на кнопку ниже👇',
                     parse_mode="Markdown", reply_markup=web_app_keyboard_inline())  # отправляем сообщение с нужной клавиатурой
    send_users_data(tlg_update=message)



# @bot.message_handler(content_types=["web_app_data"])  # получаем отправленные данные
# def answer(webAppMes):
#     print(webAppMes)  # вся информация о сообщении
#     print(webAppMes.web_app_data.data)  # конкретно то что мы передали в бота
#     bot.send_message(webAppMes.chat.id, f"получили инофрмацию из веб-приложения: {webAppMes.web_app_data.data}")
#     # отправляем сообщение в ответ на отправку данных из веб-приложения


if __name__ == '__main__':
    logger.success(f'СТАРТ БОТА!')
    bot.infinity_polling()

