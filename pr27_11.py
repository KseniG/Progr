class Furniture:
    def __init__(self, height, width, lenght):
        self.height = height
        self.width = width
        self.lenght = lenght
    def get_info(self):
        print("Это мебель")

class Table(Furniture):
    def __init__(self, height, width, lenght, form):
        super().__init__(height, width, lenght)
        self.form = form
    def square(self):
        return self.height*self.width*self.lenght
    def get_info(self):
        print("Это стол")

table = Table(0.6,1.5,1, 'круг')
print(table.square())
print(table.form)
test_fur = Furniture(0.6,0.5,1)

test_fur.get_info()
table.get_info()

####################################

class Goods:
    def __init__(self, name, weight, price):
        print("init MixinLog")
        super().__init__() #Добавили, чтобы тетрадь получила id Это ссылка "поищи ещё один Init в родителях"
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name},{self.weight}, {self.price}")

class MixinLog:
    ID = 0

    def __init__(self):
        print("init MixinLog")
        self.ID += 1
        self.id = id

    def save_sell_log(self):
        print(f"{self.id} продан в 00ч:00мин")

class NoteBook(Goods, MixinLog):
    pass
