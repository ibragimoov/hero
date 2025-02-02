class Hero:
    hp = 100
    attack = 15

    def eat(self):
        print('Герой ест')

    def sleep(self):
        print('Герой спит')

    def make_attack(self):
        print('Герой атакует')

hero1 = Hero()

class Enemy:
    hp = 50
    attack = 7