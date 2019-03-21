import time
import schedule

class Event:
    def __init__(self, amount, cost, host, info):
        self.amount = amount
        self.cost = cost
        self.host = host
        self.info = info
        self.book = 0

    def booking(self, number, ):
        self.amount = self.amount - number
        self.book = self.book + number


    def provebooking(self):
        pass


class User:
    def __init__(self, name, id, chat_id):
        self.name = name
        self.id = id
        self.chat_id=chat_id
