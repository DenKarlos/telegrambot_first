import telebot
import config
from random import randint
from telebot import types

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open("static/sticker.webp", "rb")
    bot.send_sticker(message.chat.id, sti)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Рандомное число')
    item2 = types.KeyboardButton('Тебе хорошо? 💩')
    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     f"Welcome, {message.from_user.first_name}!\nI'm {bot.get_me().first_name} bot, that greeting you",
                     parse_mode='html', reply_markup=markup)

    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton('Рандомное число')
    # item2 = types.KeyboardButton('🥰Как дела?')
    # markup.add(item1, item2)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(randint(1, 10**6)))
        elif message.text == 'Тебе хорошо? 💩':
            bot.send_message(message.chat.id, 'Сходи в туалет!')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😒')


bot.polling(none_stop=True)


# @bot.message_handler(commands=['start'])
# def welcome(message):
#     sti = open('static/AnimatedSticker.tgs', "rb")
#     bot.send_sticker(message.chat.id, sti)
