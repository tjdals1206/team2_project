class ComputerPlayer:

    def __init__(self):
        self.balance = 5000  # 컴퓨터의 현재 잔고
        self.place = 0  # 컴퓨터의 현재 위치
        self.owner = ""  # 위치한 도시의 소유주
        self.city_name = ""  # 위치한 도시의 이름
        self.name = "computer"  # 플레이어 이름
        
    def getPlace(self, place, owner):  # 컴퓨터가 위치한 도시 인덱스 값, 도시 이름, 소유주를 받아 옴
        self.place = place
        self.owner = owner
        self.city_name = city_name[place]
        
    def move(self):  # 주사위를 굴려서 이동해야 하는 인덱스를 반환함
        dice = random.randint(1, 6)  # 랜덤 함수를 이용해서 1, 6사이의 랜덤한 숫자를 반환함
        print("컴퓨터가 주사위를 굴렸습니다. " + dice + "만큼 이동합니다.")
        self.place += dice  # 위치 인덱스에 결과값을 더함
        return self.place

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