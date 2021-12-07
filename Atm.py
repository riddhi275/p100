class Atm:
    def _init_(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("balance is $50,000")
    def withdrawl(self, amount):
        new_amount = 50000-amount
        print("You have withdrawn amount"+str(amount)+". Your remaining balance is"+ str(new_amount))

def main():
    cardnumber = input("insert your card number")
    pin = input("insert your pin number")
    new_user = Atm(cardnumber, pin)
    print("choose your activity")
    print("1. balance inquiry 2. withdrawl")
    activity = int(input("enter activity number:"))

    if(activity == 1):
        new_user.check_balance

    elif(activity == 2):
        new_user.withdrawl
    
    else:
        print("enter valid")

main()