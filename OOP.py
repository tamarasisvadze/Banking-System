class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
            return "personal details"
            return f'"Name": {self.name},"Age": {self.age},"Gender": {self.gender}'

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0
  
    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + amount
        return f"Account balance has been updated : {self.balance}"
    
    def withdrow(self,amount):
        self.amount = amount
        if (self.amount  > self.balance):
            return f"it'sInsufficient ,Balance Avalieble {self.balance}"
        else:
            self.balance = self.balance - self.amount
            return f"Account balance has been updated : {self.balance}"

    def view_balance(self):
        self.show_details() 
        return f"Account balance : {self.balance}"

person_1 = User("tamari",19,"Female")
print(person_1.show_details)
person_2 = Bank("Mishka",16,"Male")
amount = int(input("ramdenis gatana gsurt?"))
print(person_2.deposit)
