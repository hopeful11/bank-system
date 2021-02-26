class Atm:
    def __init__(self):
        self.account_list = []
        self.account_amount = 0

    def open_a_bank_account(self, name, password):
        self.account_list.append( Account(name, password, self.account_amount) )
        self.account_amount += 1

    def login(self, name, password):
        for obj in self.account_list:
            if obj.name == name and obj.password == password:
                return obj
        return None


class Account:
    def __init__(self, name, password, id):
        self.name = name
        self.password = password
        self.id = id
        self.balance = 0

    def withdraw(self,amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        print(self.balance)

    def transfer(self, reciever, amount):
        self.balance -= amount
        reciever.balance += amount

    def change_account_information(self, name, password):
        self.name = name
        self.password = password

    def delete_account(self):
        pass

    def return_to_main_menu(self):
        pass

a = Atm()
a.open_a_bank_account("mary","123pasd123")
b = a.login("mary", "123pasd123")
print(b.name)
