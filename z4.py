class Product:
    def __init__ (self, name, price):
        self.name = name
        self.price = price


class Order:

    def __init__(self):
        self.id = id(self)
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_total_price(self):
        price = sum (product.price for product in self.products)
        return price



    def display_order(self):
        print (f"Номер заказа: {self.id}")

        if not self.products:
            print("Корзина пуста")
            return

        print("Список товаров:")
        for i in range(len(self.products)):
            product = self.products[i]
            print(f"{product.name} | {product.price} руб.")
        total_price = self.get_total_price()
        print(f"ИТОГО: {total_price} руб.")

p1 = Product("Колбаса", 500.00)
p2 = Product("Горошек зелёный", 250.50)
p3 = Product("Картофель", 50.5)
p4 = Product("Морковь", 32.10)
p5 = Product("Яйцо", 140.00)

order1 = Order()
order1.add_product(p1)
order1.add_product(p2)
order1.add_product(p3)
order1.display_order()
order2 = Order()
order2.add_product(p4)
order2.add_product(p5)
order2.display_order()

order1.add_product(p4)
order1.display_order()
print(f"Общая стоимость заказа {order1.id}: {order1.get_total_price():.2f} руб.")
print(f"Общая стоимость заказа {order2.id}: {order2.get_total_price():.2f} руб.")
