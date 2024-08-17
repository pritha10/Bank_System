
class locker:
    def deposit(self, balance):
       amount = int(input("enter the amount to be input: "))
       balance = balance + amount
       print("Money deposited successfully")
       print("The current balance is: ",balance)
       return balance

    def withdraw(self, balance):
        money = int(input("enter the money to be withdraw: "))
        if money > balance:
            print("no sufficient amount is present in the account")
        else:
            balance=balance-money
            print("money is withdrawn successfully")
            print("Current Balance = ", balance)
        return balance

    def item(self):
        print(" you want to keep  gold ")
        print("gold kept succesfully")


class Bank(locker):
    def __init__(self):
        self.name = ""
        self.address = ""
        self.age = ""
        self.password = ""
        self.balance = 0
        print("account is created")
    def customerdetails(self): 
        self.name =str(input("enter the name of the customer:"))
        self.address =str(input("enter the address of the customer:"))
        self.age= int(input("eneter the age of the customer:"))
        self.password = input("Enter Password: ")
        print("the customer details is :",self.name, self.address, self.age)

        while True:
            choice = input("Deposit or Withdraw or Log Out: ")
            
            if choice.lower() == "deposit":
                self.balance = super().deposit(self.balance)
                
            elif choice.lower() == 'withdraw':
                self.balance = super().withdraw(self.balance)

            elif choice.lower() == "log out":
                
                print("sucessfully logout")
            break

        else:
                print("Wrong Choice")


if __name__=="__main__":
    account=Bank()
    account.customerdetails()

    