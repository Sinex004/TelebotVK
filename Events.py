import time

class Event:
    def __init__(self, name, amount, cost, host, info):
        self.name = name   #name of event
        self.amount = amount
        self.cost = cost
        self.host = host
        self.info = info  # date and other information
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
