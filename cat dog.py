import random

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.x = random.randint(-100,100)
        self.y = random.randint(-100,100)

    def make_sound(self):
        print('Hi!')

    def get_position(self):
        return f'({self.x};{self.y})'

    def run(self, x, y):
        self.x += x
        self.y += y


class Cat(Animal):
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog(Animal):
    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")

class Bird(Animal):
    def info(self):
        print(f"I am a bird. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Tweet")

cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)
bird1 = Bird("Poppy", 3)

for animal in (cat1, dog1, bird1):
    animal.make_sound()
    animal.info()
    print(animal.get_position())
    animal.run(random.randint(-50,50), random.randint(-50,50))
    print(f'Новое место: {animal.get_position()}')
