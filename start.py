from config import API_TOKEN
from joke import take_joke, joke_markup, base_markup
from weather import take_weather
from bs4 import BeautifulSoup
import telebot
from telebot import types

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! это мой учебный бот, здась можно узнать анекдот или погоду в Питере".format(
                         message.from_user), reply_markup=base_markup())


@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "Узнать погоду":
        weather = take_weather()
        bot.send_message(message.chat.id, text=f'Температура сегодня: {weather["fact"]["temp"]} градусов')
    elif message.text == "Рассказать анекдот":
        bot.send_message(message.chat.id, text="Выбери, что хочешь узнать", reply_markup=joke_markup())
    elif message.text == "Анекдот":
        joke = BeautifulSoup(take_joke(1), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Рассказы":
        joke = BeautifulSoup(take_joke(2), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Стишки":
        joke = BeautifulSoup(take_joke(3), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Афоризмы":
        joke = BeautifulSoup(take_joke(4), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Цитаты":
        joke = BeautifulSoup(take_joke(5), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Тосты":
        joke = BeautifulSoup(take_joke(6), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Статусы":
        joke = BeautifulSoup(take_joke(8), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Анекдот (+18)":
        joke = BeautifulSoup(take_joke(11), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Рассказы (+18)":
        joke = BeautifulSoup(take_joke(12), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Стишки (+18)":
        joke = BeautifulSoup(take_joke(13), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Афоризмы (+18)":
        joke = BeautifulSoup(take_joke(14), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Цитаты (+18)":
        joke = BeautifulSoup(take_joke(15), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Тосты (+18)":
        joke = BeautifulSoup(take_joke(16), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Статусы (+18)":
        joke = BeautifulSoup(take_joke(18), features="xml")
        bot.send_message(message.chat.id, text=joke.text, reply_markup=joke_markup())
    elif message.text == "Вернуться в главное меню":
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=base_markup())


bot.polling(none_stop=True)

