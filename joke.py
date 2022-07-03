import requests
import telebot
from telebot import types


def base_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Узнать погоду")
    btn2 = types.KeyboardButton("Рассказать анекдот")
    markup.add(btn1, btn2)
    return markup


def take_joke(choice):
    res = requests.get(f'http://rzhunemogu.ru/Rand.aspx?CType={choice}')
    if res:
        return res.text
    else:
        print('Response Failed')


def joke_markup():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Анекдот")
    btn2 = types.KeyboardButton("Рассказы")
    btn3 = types.KeyboardButton("Стишки")
    btn4 = types.KeyboardButton("Афоризмы")
    btn5 = types.KeyboardButton("Цитаты")
    btn6 = types.KeyboardButton("Тосты")
    btn7 = types.KeyboardButton("Статусы")
    btn8 = types.KeyboardButton("Анекдот (+18)")
    btn9 = types.KeyboardButton("Рассказы (+18)")
    btn10 = types.KeyboardButton("Стишки (+18)")
    btn11 = types.KeyboardButton("Афоризмы (+18)")
    btn12 = types.KeyboardButton("Цитаты (+18)")
    btn13 = types.KeyboardButton("Тосты (+18)")
    btn14 = types.KeyboardButton("Статусы (+18)")
    back = types.KeyboardButton("Вернуться в главное меню")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, back)
    return markup
