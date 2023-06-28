class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} is loaded.".format(self.name))
        print("HP : {0}\tATK = {1}".format(self.hp, self.damage))

marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank = Unit("Tank", 150, 55)