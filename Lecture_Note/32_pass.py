# 건물
#일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # name, hp, damage가 맴버 변수.
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1}\t 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))
        

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage): # name, hp, damage가 맴버 변수.
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1}\t 방향으로 적군을 공격. [ATK : {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1}\t 데미지를 입었습니다. ".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다. ".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} : Dead".format(self.name))

# 날 수 있는 기능을 가진 유닛에 대한 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1}\t 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed는 0
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass # 아무 것도 하지 않고 넘어 가겠다.

#서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")