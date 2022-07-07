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
        
    #Board는 아래와 같이 출력됩니다.
    #| 도시이름 |
    #| 도시주인 |
    #| 도시가격 |
    #| 플레이어 유무 |
        def print_board(self):
        for i in city_name[10:17]:
            print(" ------------- ".center(13), end='\t')
        print()
        for i in city_name[10:17]:
            print("|" + globals()[i].name.center(13) + "|", end='\t')
        print()
        for i in city_name[10:17]:
            print("|" + globals()[i].owner.center(13)+ "|", end='\t')
        print()
        for i in city_name[10:17]:
            print("|" + str(globals()[i].price).center(13)+ "|", end='\t')
        print()
        for i in city_name[10:17]:
            print("|" + globals()[i].place.center(13)+ "|", end='\t')
        print()
        for i in city_name[10:17]:
            print(" ------------- ".center(13), end='\t')
        print()

        print(" ------------- ".center(13), end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print(" ------------- ".center(13))
        print("|" + Sydney.name.center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print("|" + Paris.name.center(13) + "|")
        print("|" + Sydney.owner.center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print("|" + Paris.owner.center(13) + "|")
        print("|" + str(Sydney.price).center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print("|" + str(Paris.price).center(13) + "|")
        print("|" + Sydney.place.center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print("|" + Paris.place.center(13) + "|")
        print(" ------------- ".center(13), end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print(" ------------- ".center(13))

        print(" ------------- .center(13), end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print(" ------------- ".center(13))
        print("|" + Tokyo.name.center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print("|" + New_York.name.center(13) + "|")
        print("|" + Tokyo.owner.center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print("|" + New_York.owner.center(13) + "|")
        print("|" + str(Tokyo.price).center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print("|" + str(New_York.price).center(13) + "|")
        print("|" + Tokyo.place.center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print("|" + New_York.place.center(13) + "|")
        print(" ------------- ".center(13), end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print(" ------------- ".center(13))

        print(" ------------- ".center(13), end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print(" ------------- ".center(13))
        print("|" + Bali.name.center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print("|" + Seoul.name.center(13) + "|")
        print("|" + Bali.owner.center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print("|" + Seoul.owner.center(13) + "|")
        print("|" + str(Bali.price).center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print("|" + str(Seoul.price).center(13) + "|")
        print("|" + Bali.place.center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print("|" + Seoul.place.center(13) + "|")
        print(" ------------- ".center(13), end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print(" ------------- ".center(13))

        for i in city_name[0:7]:
            print(" ------------- ".center(13), end='\t')
        print()
        for i in reversed(city_name[0:7]):
            print("|" + globals()[i].name.center(13) + "|", end='\t')
        print()
        for i in reversed(city_name[0:7]):
            print("|" + globals()[i].owner.center(13)+ "|", end='\t')
        print()
        for i in reversed(city_name[0:7]):
            print("|" + str(globals()[i].price).center(13)+ "|", end='\t')
        print()
        for i in reversed(city_name[0:7]):
            print("|" + globals()[i].place.center(13)+ "|", end='\t')
        print()
        for i in reversed(city_name[0:7]):
            print(" ------------- ".center(13), end='\t')
        print()

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
    
    
    
while True:
    board = Board()
    player = Player()
    computer = ComputerPlayer()
    board.print_board()
    player.move()
    if city_name[player.place] == "empty":
        player.buy()
    else:
        player.pay()
        computer.receive()
    player.is_bankrupt()
    computer.move()
    if city_name[computer.place] == "empty":
        computer.buy()
    else:
        computer.pay()
        player.receive()
    computer.is_bankrupt()