class Atm:
    def __init__(self, account_list):
        self.account_list = account_list
        self.loop()

    def open_a_bank_account(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        self.account_list.append( Account(name, password, 0) )

    def login(self):
        found = False
        for i in range(3):
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            found = False
            for obj in self.account_list:
                if obj.name == name and obj.password == password:
                    found = True
                    is_del = obj.loop(self.account_list)
                    if is_del == True:
                        self.account_list.remove(obj)
            if found == False:
                print("Wrong combination, please try again")
            else: break
        if found == False:
            print("3 in a row, you got kicked mate!")

    def loop(self):
        while(1):
            option = input("""Welcome:
    1) Open a bank account
    2) Login
    3) Exit
""")
            if option == '1':
                self.open_a_bank_account()
            elif option == '2':
                self.login()
            elif option == '3':
                return 0
            else:
                print("I'm sorry, that is not a valid option\n")

class Account:
    def __init__(self, name, password, balance):
        self.name = name
        self.password = password
        self.balance = balance

    def withdraw(self):
        while True:
            try:
                amount = int(input("Enter the amount: "))
                if self.balance >= amount:
                    self.balance -= amount
                else:
                    print("Your balance is insufficient!")
                    break
            except ValueError:
                print("Please enter a number!")

    def deposit(self):
        while True:
            try:
                amount = int(input("Enter the amount: "))
                if amount >= 0:
                    self.balance += amount
                else:
                    print("You must deposit positif amount of money!")
                    continue
            except ValueError:
                print("Please give a number!")
            else:
                break

    def get_balance(self):
        print(self.balance)

    def transfer(self):
        while True:
            name = input("Who would you like to transfer to: ")
            obj = 0
            for temp in self.account_list:
                if temp.name == name:
                    obj = temp
                    break
            if obj == 0:
                print("Please enter an exist customer name!")
            else:
                break

        while True:
            try:
                amount = int(input("Enter the amount: "))
                if amount >= 0:
                    self.balance -= amount
                    obj.balance += amount
                else:
                    print("You must transfer positif amount of money!")
                    continue
            except ValueError:
                print("Please give a number!")
            else:
                return

    def change_account_information(self):
        name = input("Enter your new name: ")
        password = input("Enter your new password: ")
        self.name = name
        self.password = password
        print(f"Your new name is: {self.name}\nNew password is: {self.password}")

    def delete_account(self):
        return True

    def loop(self, account_list):                       #for to see other account to transfer
        self.account_list = account_list

        while(1):
            temp = input(f"""This is {self.name}'s account:
    1) withdraw
    2) deposit
    3) get balance
    4) transfer money
    5) change account information
    6) delete account
    7) return to main menu
""")
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
                return self.delete_account()
            elif temp == '7':
                return False
            else:
                print("Please enter a valid option!")

def set_account_list(account_file):
    account_list = []
    for lines in account_file.readlines():
        account_data = lines.split(",")     #name pass balance
        account_list.append( Account(account_data[0], account_data[1], int(account_data[2][:-1])) ) #"\n"
    return account_list

def end_account_file(account_file, account_list):
    account_file.seek(0)
    for i in account_list:
        account_file.write(f"{i.name},{i.password},{i.balance}\n")

def main():
    with open("./accounts.txt", "r+") as account_file:
        account_list = set_account_list(account_file)
    Atm(account_list)
    with open("./accounts.txt", "w+") as account_file:
        end_account_file(account_file, account_list)

if __name__ == "__main__":
    main()

















