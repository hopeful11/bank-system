class Bank:                                      #class silinebilir
    account_list = []
    account_file = open("accounts.txt", "w+")

class ATM(Bank):
    def __init__(self, account_list):
        self.account_list=account_list
        self.loop()

    def loop(self):
        while True:
            option=input("""welcome,enter your choice.
             1=open an account
             2=login
             3=exit""")

            if option=="1":
                self.open_an_account()
            elif option=="2":
                self.login()
            elif option=="3":
                self.exit()
            elif option!="1"and "2" and "3":
                print("I'm sorry, that is not an option\n")
            else:
                pass

    def open_an_account(self):                               #balance eklenilecek
        name=input("please enter your name")
        password=input("please enter your password")
        self.account_list.append(Account(name, password))


    def login(self):
        name = input("please enter your name:")
        password = input("please enter your password:")
        for obj in self.account_list:
            if  obj.name == name and obj.password == password:
                 is_del = obj.loop(self.account_list)
                 if is_del == True:
                     self.account_list.remove(obj)


    def exit(self):
        exit()

class Account:
    def __init__(self,name,password,balance):
        self.name=name
        self.password=password
        self.balance=balance

    def loop(self,account_list):
        self.account_list = account_list
        while True:
            option=input("""welcome,enter your choice.
                         1=withdraw
                         2=deposit
                         3=get balance
                         4=transfer
                         5=change account information
                         6=delete the account
                         7=return to main menu""")
            if option == "1":
                self.withdraw()
            elif option == "2":
                self.deposit()
            elif option == "3":
                self.get_balance()
            elif option == "4":
                self.transfer()
            elif option == "5":
                self.change_account_information()
            elif option == "6" :
                return 1
            elif option == "7" :
                return 0
            elif option!="1"and "2" and "3" and "4" and "5" and "6" and "7":
                print("I'm sorry, that is not an option\n")

    def withdraw(self):
       while True:
        try:
           amount = int(input("enter the amount"))
           if self.balance > amount:
                self.balance-=amount
           else:
               print("your balance is insufficient\n")
        except ValueError:
            print("You entered wrong value\n")
        else:
            break

    def deposit(self):
       while True:
        try:
           amount = int(input("enter amount"))
           self.balance+=amount
        except ValueError:
            print("You entered wrong value\n")
        else:
            break

    def get_balance(self):
        print(self.balance)

    def transfer(self):
        name=(input("Who you like to transfer to:"))
        amount=int(input("enter the amount"))
        for i in self.account_list:
             if i.name == name:
                 self.balance = str(int(self.balance) - amount)
                 i.balance = str(int(i.balance) + amount)
                 return

    def change_account_information(self):
        new_name=input("enter your newname")
        new_password=input("enter your newpassword")
        self.name=new_name
        self.password=new_password
        print("newname:",self.name,"\nnewpassword:",self.password)

    # def __del__(self):           #düzeltilecek
    #     print("Account deleted")
    #     return 0

    def set_account_list(account_file):
        account_list = []
        for lines in account_file.readlines():
            account_data = lines.split(",")
            account_list.append( Account(account_data[0], account_data[1], account_data[2][:-1]))
        return account_list

    def end_account_file(account_file, account_list):
        account_file.seek(0)
        for i in account_list:
            account_file.write(f"{i.name},{i.password},{i.balance}\n")

    if __name__ == "__main__":
        with open("./accounts.txt", "r+") as account_file:
            account_list = set_account_list(account_file)
        ATM(account_list)
        with open("accounts.txt", "w+") as account_file:
            end_account_file(account_file, account_list)

