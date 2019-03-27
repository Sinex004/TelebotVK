# import os
import telebot
# from flask import Flask, request
from telebot import types
from Events import User
from Facade import BotFacade

global dict_users, events
dict_users = {}
events = {}
# server = Flask(__name__)
# bot = telebot.TeleBot(misc.token)

facade = BotFacade()
bot = facade.getBot()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'Здарствуйте, ' + message.from_user.first_name + "! Введите свое ID")
    bot.register_next_step_handler(message, process_id)


def process_id(message):
    global dict_users
    u = User(name=message.from_user.first_name, id=message.text, chat_id=message.from_user.id)
    dict_users[message.from_user.id] = u


@bot.message_handler(commands=['Event'])
def handle_event(message):
    # список ивентов сделай, сперва заполни их в словарь events
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row('Date')
    user_markup.row('Booking')
    user_markup.row('Info')
    bot.send_message(message.from_user.id, 'Что Вы хотите ?', reply_markup=user_markup)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@bot.message_handler(commands=['Phone'])
def phone(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, "Отправь мне свой номер телефона для брони", reply_markup=keyboard)
# @server.route('/' + misc.token, methods=['POST'])
# def getMessage():
#     bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     return "!", 200
#
#
# @server.route("/")
# def webhook():
#     bot.remove_webhook()
#     bot.set_webhook(url='https://telebotvk.herokuapp.com/'+ misc.token)
#     return "!", 200
#
# bot.enable_save_next_step_handlers(delay=2)
# bot.load_next_step_handlers()


if __name__ == '__main__':
    facade.startBot()
    # bot.remove_webhook()
    # bot.polling()
    # server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
