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

    def buy(self,price,city_name): #이동한 도시가 비어있고, 잔고 충분하다면 도시를 구매
        if self.balance >= price:
            print(self.name + " 이(가) " + self.city_name + "을(를) 구매했습니다.")
            self.balance -= price
            print(self.name + "의 잔고가 " + self.balance + "만큼 남았습니다.")
        else:
            print("잔고가 부족합니다. 도시를 구매하지 못했습니다.")
    
    def pay(self,price): #이동한 도시의 주인이 있을 때 통행료을 지불하고 잔고가 부족하다면 표시
        if self.owner == "player":
            if self.balance >= price:
                print(self.name + "이(가)" + self.city_name + "을(를) 구매했습니다.")
                self.balance -= price
                print(self.name + " 의 잔고가 " + self.balance + "만큼 남았습니다.")
            else:
                print("잔고가 부족합니다."+ self.name + "이(가) 대금을 지불하지 못했습니다.")

    def pay(self):

    def receive(self):

    def is_bankrupt(self):