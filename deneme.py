class Account:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0

    def __del__(self):
        pass

    def withdraw(self,amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        print(self.balance)

    def transfer(self, reciever, amount):
        self.balance -= amount
        reciever.balance += amount

    def change_account_information(self):
        pass
    def delete_account(self):
        self.__del__()
    def return_to_main_menu(self):
        pass

a = Account("mary", 1556)
b = Account("ahmet", 5445)
a.deposit(500)
a.transfer(b,200)
a.delete_account()
a.get_balance()