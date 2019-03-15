import os

import telebot
from flask import Flask, request

import misc


server = Flask(__name__)
bot = telebot.TeleBot(misc.token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message,message.text)


@server.route('/' + misc.token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your_heroku_project.com/' + misc.token)
    return "!", 200


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__=='__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
