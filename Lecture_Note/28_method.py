class Unit:
    def __init__(self, name, hp, damage): # name, hp, damage가 맴버 변수.
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} is loaded.".format(self.name))
        print("HP : {0}\tATK = {1}".format(self.hp, self.damage))

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage): # name, hp, damage가 맴버 변수.
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1}\t 방향으로 적군을 공격. [ATK : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1}\t 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다. ".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : Dead".format(self.name))

# 파이어뱃 : 공격 유닛, 화염방사기
firebat1 = AttackUnit("FireBat", 50, 16)
firebat1.attack("5시")

# 공격을 두번 받았다고 가정
firebat1.damaged(25)
firebat1.damaged(25)