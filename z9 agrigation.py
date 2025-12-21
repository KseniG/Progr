import math
import os
# Agrigation (using class in other class)
class Win_Door:
    def __init__(self,x,y):
        self.square = x*y

class Room:
    def __init__(self,x,y,z):
        self.__width = x
        self.__height = z
        self.__lenght = y
        self.__win_door = []
        self.square_calc()

    def square_calc(self):
        self.square = (self.__width*self.__height*2+self.__height*self.__lenght*2)

    def get_square(self):
        print(self.square)

    def add_win_door(self, x, y):
        self.__win_door.append(Win_Door(x,y))
    def effective_square(self):
        work_square = self.square
        for i in self.__win_door:
            work_square -= i.square
        return work_square
'''
room = Room(4,5,3)
room.add_win_door(2,2)
room.add_win_door(1,0.8)
print(room.effective_square())
'''

#### Composition (creating class in class for using)

class Roll:
    def __init__(self,x,y):
        self.__width = x
        self.__lenght = y
        self.square = x*y

    def get_square(self):
        return self.square

class Room:
    class __Win_Door:
        def __init__(self,x,y):
            self.square = x*y

    def __init__(self,x,y,z,c):
        self.__width = x
        self.__height = z
        self.__lenght = y
        self.__count = c
        self.__win_door = []
        self.square_calc()

    def get_count(self):
        return self.__count

    def square_calc(self):
        self.square = (self.__width*self.__height*2+self.__height*self.__lenght*2)

    def get_square(self):
        return self.square

    def add_win_door(self, x, y):
        self.__win_door.append(self.__Win_Door(x,y))
    def effective_square(self):
        work_square = self.square
        for i in self.__win_door:
            work_square -= i.square
        return work_square
    def calc_rools(self, roll):
        return self.effective_square()/roll.get_square()

# bad - wd = Room.Win_Door(4,4)
room = Room(4,5,3,int(input('Введите кол-во окон/дверей: ')))
print('Вводите параметры окон/дверей через пробел')
for i in range(room.get_count()):
    x,y = map(float, input().split())
    room.add_win_door(x,y)


d = 5
instr = 'Введите:\n1 - расчёт полной площади\n2-расчёт реальной площади\n3 - расчёт кол-ва обоев\n0 - завершить программу\n10 - очистить консоль'
print(instr)
while d!= 0:
    d = int(input())
    match d:
        case 0:
            break
        case 1:
            print(f'Полная площадь: {room.get_square()}')
        case 2:
            print(f'Рабочая площадь: {room.effective_square()}')
        case 3:
            x,y = map(float, input('Введите ширину и длину рулона обоев: ').split())
            roll = Roll(x,y)
            print(math.ceil(room.calc_rools(roll)))
        case 10:
            os.system('cls')
            print(instr)
