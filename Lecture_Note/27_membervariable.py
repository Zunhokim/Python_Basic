class Unit:
    def __init__(self, name, hp, damage): # name, hp, damage가 맴버 변수.
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} is loaded.".format(self.name))
        print("HP : {0}\tATK = {1}".format(self.hp, self.damage))

# marine1 = Unit("Marine", 40, 5)
# marine2 = Unit("Marine", 40, 5)
# tank = Unit("Tank", 150, 55)

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)

wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 파이썬에서는 어떤 객체에 외부 변수를 추가해서 사용 할 수 있음. 
# 외부 변수를 추가할 경우, 할당한 개체에 한하여 적용됨. 