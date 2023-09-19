#Due to lack of time, the password feature could not be fully implemented. It is an extra feature.
#Due to lack of time, this code has not been rigourously tested and may have errors in edge cases.
import random as r
import getpass as gp
import time
class Bank:
    l = []
    def start(self):
        self.temp = ''
        exec(f"self.a{self.temp} = Vault.create({self.temp})")
    @property
    def temp(self):
        return self._temp
    @temp.setter
    def temp(self, temp):
        if temp in self.l or not temp:
            temp = str(r.randint(90000000, 99999999))
            self.temp = temp
        else:
            self.l.append(temp)
            self.l = list(set(self.l))
            self._temp = temp
    @classmethod
    def menu(cls):
        while True:
            print('''a) Create account
b) Deposit money
c) Withdraw money
d) Account summary
e) Exit''')
            match input("Enter option: "):
                case "a":
                    b.start()
                case "b":
                    inp = input("Enter account number: ")
                    exec(f"b.a{inp}.deposit()")
                case "c":
                    inp = input("Enter account number: ")
                    exec(f"b.a{inp}.withdraw()")
                case "d":
                    inp = input("Enter account number: ")
                    exec(f"b.a{inp}.acc_sum()")
                case _:
                    exit()
class Vault(Bank):
    l = []
    def __init__(self, name, acc_no, passwd):
        self.name = name
        self.acc_no = acc_no
        self.passwd = passwd
        self.bal = 0
        print("Account created with the following details:",
              f"name: {self.name}\nAccount number: {self.acc_no}",
              "password: " + "*"*len(self.passwd),
              f"balance: {self.bal}", sep = "\n")
    @classmethod
    def create(cls, acc_no):
        name = input("Enter name: ")
        acc_no = acc_no
        #passwd = gp.getpass("Enter password: ")
        passwd = input("Enter password: ")
        return cls(name, acc_no, passwd)
    @property
    def acc_no(self):
        return self._acc_no
    @acc_no.setter
    def acc_no(self, acc_no):
        if acc_no in self.l or not acc_no:
            acc_no = str(r.randint(90000000, 99999999))
            self.acc_no = acc_no
        else:
            self.l.append(acc_no)
            self.l = list(set(self.l))
            self._acc_no = acc_no

    def deposit(self):
        print(f"current balance: {self.bal}")
        self.deposit = int(input("Enter money to be deposited: "))
        self.bal += self.deposit
        print(f"Transaction sucessfull. New balance: {self.bal}")
    def withdraw(self):
        self.withdraw = int(input("Enter money to be withdrawn: "))
        self.bal -= self.withdraw
        print(f"Transaction sucessfull. New balance: {self.bal}")
    def acc_sum(self):
        print("Account has the following details:",
              f"name: {self.name}\nAccount number: {self.acc_no}",
              "password: " + "*"*len(self.passwd),
              f"balance: {self.bal}", sep = "\n")
    
b = Bank()
b.menu()