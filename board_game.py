class ComputerPlayer:

    balance = 5000
    place = ""

    def move(self):

    def buy(self):

    def pay(self):

    def receive(self):

    def is_bankrupt(self):


city_name = ["Start"]

class Board:
    def __init__(self):
        self.city = []
        self. player = []
        self.create()

    def create(self):
        for i in city_name:
            self.city.append(i)


class Player: #real player
    def __init__(self):
        self.name = ""
        self.place = 0
        self.balance = 5000
        self.owner = ""
        self.city_name = ""
    
    def getName(self):
        return self.name
    
    def getPlace(self):
        return self.place
    
    def getBalance(self):
        return self.balance

    def move(self):

    def buy(self):

    def pay(self):

    def receive(self):

    def is_bankrupt(self):