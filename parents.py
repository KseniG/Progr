'''Написаь систему классов существ в игре'''

class Unit:
    def __init__(self, name, hp):
        self._name = name
        self._hp=hp
    def get_name(self):
        print(self.name)
    def get_damage(self, damage):
        if damage<0:
            print('Ошибка!')
        elif self._hp<=damage:
            print('Mission failed')
        else:
            self._hp -= damage
    def get_heal(self, heal):
        self._hp += heal

class Enemy(Unit):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self._damage = damage
    def hit():
        pass

class NPC(Unit):
    def __init__(self, name, hp):
        super().__init__(name, hp)
    def tell():
        print('Hello!')

class Character(Unit):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self.damage = damage
        self.inventory = []

my_enemy = Enemy('Lazyness', 1000, 10)
my_character = Character('Геральд', 35, 15)
shop_keeper = NPC('John', 1)

my_enemy.get_name()
my_character.get_heal(10)
