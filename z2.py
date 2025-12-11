class BankAccount:
    def __init__(self, number):
        self.__balance = 0
        self.__accNumber = number
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
    def get_accNumber(self):
        return self.__accNumber
    def withdraw(self, amount):
        try:amount = int(amount)
        except ValueError: print('Ошибка! Введено некорректное значение')
        if amount>self.__balance:
            print('Недостаточно средств')
        elif amount<=0:
            print('Ошибка! Введено отрицательное значение')
        else:
            self.__balance -= amount

account = BankAccount('123498764526')
account.deposit(754)
print(account.get_accNumber())
print(account.get_balance())

account.withdraw(input())
print(account.get_balance())
account.withdraw(500)
