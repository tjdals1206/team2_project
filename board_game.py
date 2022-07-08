import random


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
        print("컴퓨터가 주사위를 굴렸습니다. " + str(dice) + "만큼 이동합니다.")
        self.place += dice  # 위치 인덱스에 결과값을 더함
        return self.place

    def buy(self, price):  # 도시가 비어 있고, 잔고가 도시 가격 이상이면 도시를 구매
        if self.balance >= price:
            print("컴퓨터가 " + self.city_name + "을(를) 구매했습니다.")
            self.balance -= price
            print("컴퓨터의 잔고가 " + str(self.balance) + "만큼 남았습니다.")
        else:
            print("잔고가 부족합니다. 도시를 구매하지 못했습니다.")

    def pay(self, price):  # 도시의 소유주가 있을 경우 도시 가격만큼 통행료를 지불
        if self.owner == "player":
            if self.balance >= price:
                print("컴퓨터가 " + self.city_name + "을(를) 구매했습니다.")
                self.balance -= price
                print("컴퓨터의 잔고가 " + str(self.balance) + "만큼 남았습니다.")
            else:
                self.balance -= price
                print("잔고가 부족합니다. 컴퓨터가 대금을 지불하지 못했습니다.")

    def receive(self, price):  # 플레이어가 컴퓨터의 도시를 방문했을 때 통행료를 받음
        self.balance += price
        print("컴퓨터가 " + str(price) + "를 받았습니다.")

    def is_bankrupt(self):  # 잔고가 0보다 작으면 파산함, 파산할 경우 false를 리턴
        if self.balance < 0:
            return False
        else:
            return True


city_name = ["Start", "Bangkok", "Beijing", "Taipei", "Dubai", "Cairo", "Madrid", "Bali", "Tokyo", "Sydney",
             "Sao_Paulo", "Prague", "Berlin", "Moscow", "Geneva", "Rome", "London", "Paris", "New_York", "Seoul"]


class Board:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    # Board는 아래와 같이 출력됩니다.
    # | 도시이름 |
    # | 도시주인 |
    # | 도시가격 |
    # | 플레이어 유무 |
    def print_board(self):
        for i in city_name[10:17]:
            print(" ------------- ".center(13), end='\t')

        print()
        for i in city_name[10:17]:
            print("|" + globals()[i].name.center(13) + "|", end='\t')
        print()
        for i in city_name[10:17]:
            print("|" + globals()[i].owner.center(13) + "|", end='\t')
        print()
        for i in city_name[10:17]:
            print("|" + str(globals()[i].price).center(13) + "|", end='\t')
        print()
        for i in city_name[10:17]:
            if len(globals()[i].place) != 0:
                x = ""
                for j in globals()[i].place:
                    x += j
                print("|" + x.center(13) + "|", end='\t')
            else:
                print("|" + "".center(13) + "|", end='\t')
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
        if len(Sydney.place) != 0:
            x = ""
            for j in Sydney.place:
               x += j
            print("|" + x.center(13) + "|", end='\t')
        else:
            print("|" + "".center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        if len(Paris.place) != 0:
            x = ""
            for j in Paris.place:
                x += j
            print("|" + x.center(13) + "|", end='\t')
        else:
            print("|" + "".center(13) + "|", end='\t')
        print()
        print(" ------------- ".center(13), end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        print(" ------------- ".center(13))

        print(" ------------- ".center(13), end='\t')
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
        if len(Tokyo.place) != 0:
            x = ""
            for j in Tokyo.place:
                x += j
            print("|" + x.center(13) + "|", end='\t')
        else:
            print("|" + "".center(13) + "|", end='\t')
        for i in range(5):
            print("".center(13), end='\t')
        if len(New_York.place) != 0:
            x = ""
            for j in New_York.place:
                x += j
            print("|" + x.center(13) + "|", end='\t')
        else:
            print("|" + "".center(13) + "|", end='\t')
        print()
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
        if len(Bali.place) != 0:
            x = ""
            for j in Bali.place:
                x += j
            print("|" + x.center(13) + "|", end='\t')
        else:
            print("|" + "".center(13) + "|", end='\t')

        for i in range(5):
            print("".center(13), end='\t')
        if len(Seoul.place) != 0:
            x = ""
            for j in Seoul.place:
                x += j
            print("|" + x.center(13) + "|", end='\t')
        else:
            print("|" + "".center(13) + "|", end='\t')
        print()

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
            print("|" + globals()[i].owner.center(13) + "|", end='\t')
        print()
        for i in reversed(city_name[0:7]):
            print("|" + str(globals()[i].price).center(13) + "|", end='\t')
        print()
        for i in reversed(city_name[0:7]):
            if len(globals()[i].place) != 0:
                x = ""
                for j in globals()[i].place:
                    x += j
                print("|" + x.center(13) + "|", end='\t')
            else:
                print("|" + "".center(13) + "|", end='\t')
        self.x = " "
        print()
        for i in reversed(city_name[0:7]):
            print(" ------------- ".center(13), end='\t')
        print()
    
    #city의 place의 위치정보를 삭제합니다.
    def delete_position(self):
        for i in city_name:
            globals()[i].place.clear()

    #city의 place에 위치정보를 넣습니다.
    def check_position(self):
        globals()[city_name[self.player.place]].place.append(" P ")     #player는 P로 표시됩니다.
        globals()[city_name[self.computer.place]].place.append(" C ")   #computer는 C로 표시됩니다.


class City:
    def __init__(self, name):
        self.name = name
        self.owner = "empty"
        self.price = 300
        self.place = []




Start = City("Start")

# city를 생성합니다. 각 city의 변수는 city name입니다.
for i in city_name:
    # Start의 owner는 nothing으로 price는 0으로 설정하였습니다.
    if i == "Start":
        Start.owner = "nothing"
        Start.price = 0
    else:
        globals()[i] = City(i)


class Player:  # real player
    def __init__(self):
        self.name = "player"
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

    def move(self):  # 1~6까지의랜덤한 주사위의 값만큼 이동
        dice = random.randint(1, 6)
        print(self.name + " 가 주사위를 굴렸습니다. " + str(dice) + "만큼 이동합니다.")
        self.place += dice

        return self.place

    def buy(self, price, city_name):  # 이동한 도시가 비어있고, 잔고 충분하다면 도시를 구매
        if self.balance >= price:
            print(self.name + " 이(가) " + self.city_name + "을(를) 구매했습니다.")
            self.balance -= price
            print(self.name + "의 잔고가 " + str(self.balance) + "만큼 남았습니다.")
        else:
            print("잔고가 부족합니다. 도시를 구매하지 못했습니다.")

    def pay(self, price):  # 이동한 도시의 주인이 있을 때 통행료을 지불하고 잔고가 부족하다면 표시
        if self.owner == "player":
            if self.balance >= price:
                print(self.name + "이(가)" + self.city_name + "을(를) 구매했습니다.")
                self.balance -= price
                print(self.name + " 의 잔고가 " + str(self.balance) + "만큼 남았습니다.")
            else:
                print("잔고가 부족합니다." + self.name + "이(가) 대금을 지불하지 못했습니다.")
    
    def receive(self, price):
        self.balance += price
        print(self.name +"이(가)" + str(price) + "를 받았습니다." )
    
    def is_bankrupt(self):
        if self.balance < 0:
            print(self.name + "이 패배했습니다")
            return False
        else:
            return True
    



while True:
    player = Player()                #player 생성
    computer = ComputerPlayer()      #computer 생성
    board = Board(player, computer)  #board 생성
    board.check_position()           #player와 computer 위치 확인
    board.print_board()              #board 출력
    board.delete_position()          #player와 computer 위치정보 삭제
    player.move()                    #player 이동
    board.check_position()           #player와 computer 위치 확인
    board.print_board()              #board 출력
    board.delete_position()          #player와 computer 위치정보 삭제
    computer.move()                  #computer 이동
    board.check_position()           #player와 computer 위치 확인
    board.print_board()              #board 출력
    break;
