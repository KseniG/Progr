class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_info(self):
        return (f"Бренд: {self.brand}, модель: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, force):
        super().__init__(brand, model)
        self.force = force

    def get_info(self):
        base_info = super().get_info()
        return(base_info + f", лошадиные силы: {self.force}")

class Bicycle(Vehicle):
    def __init__(self, brand, model, type):
        super().__init__(brand, model)
        self.type = type

    def get_info(self):
        base_info = super().get_info()
        return(base_info + f", тип: {self.type}")

vehicle1 = Vehicle("Generic", "Transport")
car1 = Car("BMW", "X4", 510)
car2 = Car('Лада', 'Седан', 106)
car3 = Car("Ford", "Mustang", 315)
bike1 = Bicycle("Trek", "FX 3", "городской")
bike2 = Bicycle("Giant", "Talon", "горный")

vehicles = [vehicle1, car1, car2, car3, bike1, bike2]

print('Транспортный парк:')
for i, vehicle in enumerate(vehicles, 1):
    print(f"{i}. {vehicle.get_info()}")
