class Atm:
    def __init__(self, account_file):
        self.account_list = []
        self.account_file = account_file
        self.loop()

    def open_a_bank_account(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        self.account_list.append( Account(name, password) )
        self.account_file.write(f"{name},{password}\n")

    def login(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        for obj in self.account_list:
            if obj.name == name and obj.password == password:
                obj.loop()

    def loop(self):
        while(1):
            temp = input("""Welcome:
            1) Open a bank account
            2) Login
            3) Exit""")

            if temp == '1':
                self.open_a_bank_account()
            elif temp == '2':
                self.login()
            elif temp == '3':
                self.exit_atm()
            else:
                pass
        pass

    def exit_atm(self):
        print("CyA")
        exit()

class Account:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.balance = 0

    def withdraw(self):
        amount = int(input("Set the amount: "))
        self.balance -= amount

    def deposit(self):
        amount = int(input("Set the amount: "))
        self.balance += amount

    def get_balance(self):
        print(self.balance)
        input()

    def transfer(self, reciever, amount):   ###need fix
        self.balance -= amount
        reciever.balance += amount

    def change_account_information(self):
        name = input("Enter your new name: ")
        password = input("Enter your new password: ")
        self.name = name
        self.password = password

    def delete_account(self):   ###need fix
        self.__del__(self)
        return

    def return_to_main_menu(self):
        return 0

    def loop(self):
        while(1):
            temp = input("""This is your account:
            1) withdraw
            2) deposit
            3) get balance
            4) transfer money
            5) change account information
            6) delete account""")
            if temp == '1':
                self.withdraw()
            elif temp == '2':
                self.deposit()
            elif temp == '3':
                self.get_balance()
            elif temp == '4':
                self.transfer()
            elif temp == '5':
                self.change_account_information()
            elif temp == '6':
                self.delete_account()
            elif temp == '7':
                return self.return_to_main_menu()

if __name__ == "__main__":
    with open("./accounts.txt", "w+") as account_file:
        a = Atm(account_file)