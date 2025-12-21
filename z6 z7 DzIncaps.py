'''Задание 1:
 Разработайте класс с полной инкапсулāøией, доступ к атрибутам которого и
изменение даннýх реализуĀтсā ùерез вýзовý методов. В обüектноориентированном программировании принāто
имена методов длā извлеùениā
даннýх наùинатþ со слова get (взāтþ), а имена методов, в которýх свойствам
присваиваĀтсā знаùениā, Ɓ со слова set (установитþ). Например, get_field,
set_field.'''

class Unit:
    '''Класс Юнита, определяет имя, урон и здоровье. Урон и здоровье в сумме всегда составляют 120,
    игрок может выбрать любое количество урона от 1 до 119. Чем больший урон - тем меньше здоровье и
    наоборот. Все поля инкапсулированы, простое присваивание не сработает'''

    def __init__(self, name, damage):
        self.__name = name
        self.__health = 120-damage
        self.__damage = damage

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def age(self, damage):
        if 0<damage<120:
            self.__damage = damage
        else:
            print ('Incorrect')

    def prin_info(self):
        print(f"Имя: {self.__name}\tУрон: {self.__damage}\tЗдоровье: {self.__health}")

hero1 = Unit('H',30)
hero1.prin_info()
hero1.__health=1000
hero1.prin_info()

''' Задание 2:
 В уроке пример с классом Natural имеет недостаток. Так при иниøиаøии
обüекта знаùение поле number корректируетсā, однако ниùего не меúает
позже за пределами класса присвоитþ ÿтому полĀ некорректное знаùение,
минуā проверку методом __test. Исправþте ÿтот недоùет, оставив
возможностþ присвоениā полĀ number за пределами класса, а также не
запреûаā обüектам заводит другие полā.'''

class Natural:
    def __init__(self, n):
        self.__origin = n
        self.__number = self.__test()

    def __test(self):
        if type(self.__origin) is int and self.__origin > 0:
            return self.__origin
        else:
            print(f"Значение {self.__origin} было преобразовано к 1")
            return 1

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self):
        self.__number = self.__test()

    def newValue(self,n):
        self.__origin = n
        self.__number = self.__test()

a = Natural(34)
b = Natural(-250)
c = Natural('Hi')

print(a.number, b.number, c.number) # output: 34 1 1

a.newValue('57e8tyrbv8er')
c.newValue(10)
b.__number = 6

print(f"После преобразований: {a.number}, {b.number}, {c.number}") #output: 1 1 10
