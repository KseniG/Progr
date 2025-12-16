class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def prin_info(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


'''Не будет работать

tom = Person('Tom', 39)
print(tom.__name)
tom.prin_info()
tom.__name = 'gbfgbign'
tom.prin_info()
'''

'''Работает'''
tom = Person('Tom', 39)
tom.prin_info()
tom.__name = 'gbfgbign'
tom.prin_info()
print(tom.__name)

'''Взлом'''
print(tom.__dict__)
print(tom._Person__name)
tom._Person__name = '879687050'
tom.prin_info()

'''Get set'''
class Person2:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0<age<120:
            self.__age = age
        else:
            print ('Incorrect')
    def prin_info(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")

bob = Person2('Bob', 23)
print(bob.age)
bob.age = 40
print(bob.age)

class A:
    def __init__(self, n):
        self.a = n
        self.__x = 100 - n

    def __setattr__(self, attr, value):
        if attr in ('a', '__x'):
            self.__dict__[attr] = value
        else:
            raise AttributeError

first = A(5)
first.a = 10
first.__x = 9


print(first.__dict__)
