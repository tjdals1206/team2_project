class ComputerPlayer:

    balance = 5000
    place = ""

    def move(self):

    def buy(self):

    def pay(self):

    def receive(self):

    def is_bankrupt(self):


city_name = ["Start", "Bangkok", "Beijing", "Taipei", "Dubai", "Cairo", "Madrid", "Bali", "Tokyo", "Sydney", "Sao_Paulo", "Prague", "Berlin", "Moscow", "Geneva", "Rome", "London", "Paris", "New_York", "Seoul"]
class Board:
    def __init__(self):
        self. player = []
        
class City:
    def __init__(self, name):
        self.name = name
        self.owner = "empty"
        self.price = 300
        self.place = ""

Start = City("Start")

#city를 생성합니다. 각 city의 변수는 city name입니다.
for i in city_name:
    #Start의 owner는 nothing으로 price는 0으로 설정하였습니다.
    if i == "Start":
        Start.owner = "nothing"
        Start.price = 0
    else:
        globals()[i] = City(i)


class Player: #real player

    name = ""
    balance = 5000
    place = ""

    def getName(self):

    def getPlace(self):

    def getBalance(self):

    def move(self):

    def buy(self):

    def pay(self):

    def receive(self):

    def is_bankrupt(self):