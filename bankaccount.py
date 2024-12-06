import sys
class BankAccount():
    def __init__(self,account_holder,balance=0):
        self.account_holder = account_holder
        self.balance = balance
    def Deposit(self,amount):
        if amount >= 10:
            self.balance += amount
        else:
            print("The minimum deposit amount is $10") 
    def Withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("The withdrawal is not possible")   
Users = {
    "User1" : {
        "Username" : "alice",
        "Pin" : 1000
    },
    "User2" : {
        "Username" : "bob",
        "Pin" : 1001
    },
    "User3" : {
        "Username" : "john",
        "Pin" : 1002
    },
    "User4" : {
        "Username" : "sam",
        "Pin" : 1003
    }
}
hi = BankAccount("hi")
print(hi)
userbankaccount = None
while True:
    usernameprompt = input("Enter username: \n")
    for i in Users:
        if usernameprompt == Users[i]["Username"]:
            while True:    
                pincodeprompt = int(input("Hi "+ Users[i]["Username"]+", enter your pincode: \n"))
                if pincodeprompt == Users[i]["Pin"]:
                    name = Users[i]["Username"]
                    userbankaccount = BankAccount(name)
                    break
                else:
                    print("Your pincode is incorrect. Try again: \n")  
                    continue 
    if userbankaccount == None:
        print("Username has not been found in the system. Try again: \n")        
    else:
        print("Welcome to your bank account, here are some options you can do:")
        while True:
            ActionPrompt = input("Choose the following:\n1. Deposit \n2. Withdraw \n3. Check Balance \n4. Exit \n")
            if ActionPrompt.lower() == "deposit":
                valueprompt = int(input("How much you want to deposit? \n"))
                userbankaccount.Deposit(valueprompt)
            elif ActionPrompt.lower() == "withdraw":
                valueprompt = int(input("How much you want to withdraw? \n"))
                userbankaccount.Withdraw(valueprompt)
            elif ActionPrompt.lower() == "check balance":
                print("Currently, your account balance is $" + str(userbankaccount.balance))
            elif ActionPrompt.lower() == "exit":
                sys.exit()
