import random
class Unit:
    ID = 0
    def __init__(self, team):
        self.ID += 1
        self.id = id
        self.team = team
    def get_id(self):
        return self.id

class Soldier(Unit):
    def go_for_hero(self, target):
        print(f"{self.get_id()} follow {target.get_id()}")

class Hero(Unit):
    def __init__(self, team):
        super().__init__(team)
        self.__lvl = 0
    def levelUp(self):
        self.__lvl += 1
    def get_lvl(self):
        return self.__lvl

hero1 = Hero('Blak')
hero2 = Hero('X')

soldiersB = []
soldiersX = []
teams = ['Black', 'X']
for i in range(11):
    sold = Soldier(random.choice(teams))
    if sold.team == 'Black':
        soldiersB.append(sold)
    else:
        soldiersX.append(sold)

len1 = len(soldiersB)
len2 = len(soldiersX)
print(f"Команда {'Black'}: {len1} солдат")
print(f"Команда {'X'}: {len2} солдат")

if len1 > len2:
    hero1.levelUp()
    print(f"Увеличен уровень игрока hero1")
elif len1 < len2:
    hero2.levelUp()
    print(f"Увеличен уровень игрока hero2")

if hero1.get_lvl() > hero2.get_lvl():
    sold = random.choice(soldiersB)
    sold.go_for_hero(hero1)
elif hero1.get_lvl() < hero2.get_lvl():
    sold = random.choice(soldiersX)
    sold.go_for_hero(hero2)
