class Bank:
    account_file = open("./accounts.txt", "r+")
    account_list = []

class Atm(Bank):
    def __init__(self):
        pass

    def open_a_bank_account(self, name, password):
        self.account_list.append( Account(name, password) )
        self.account_file.write(f"{name},{password}\n")

    def login(self, name, password):
        for obj in self.account_list:
            if obj.name == name and obj.password == password:
                return obj

        for line in self.account_file.readlines():
            account_datas = line.split(",") # 0 is name and 1 is password
            print(account_datas, name, password)
            if account_datas[0] == name and account_datas[1] == password:
                print("you did it!! i think")
                self.account_file.tell()


class Account:
    def __init__(self, name, password):
        self.name = name
        self.password = password
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
#a.open_a_bank_account("mary","123pasd123")
a.login("mary","123pasd123")
#b.deposit(500)
#b.get_balance()