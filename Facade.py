import telebot
import logging
import misc
import os
from flask import Flask, request
server = Flask(__name__)


class _Logger(object):
    def __init__(self):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        logger = logging.getLogger(__name__)


class _Bot(object):
    def __init__(self):
        self.bot = telebot.TeleBot(misc.token)

    def bot_start(self):
        @server.route('/' + misc.token, methods=['POST'])
        def getMessage(self):
            self.bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
            return "!", 200

        @server.route("/")
        def webhook(self):
            self.bot.remove_webhook()
            self.bot.set_webhook(url='https://telebotvk.herokuapp.com/' + misc.token)
            return "!", 200

        self.bot.enable_save_next_step_handlers(delay=2)
        self.bot.load_next_step_handlers()

        server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

    def getBot(self):
        return self.bot


class BotFacade(object):

    def __init__(self):
        self.bot = _Bot()
        self.logger = _Logger()

    def startBot(self):
        self.bot.bot_start()

    def getBot(self):
        return self.bot.getBot()