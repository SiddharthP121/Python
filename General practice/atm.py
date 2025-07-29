class Account:
    def __init__(self, mainBalance):
        self.MB = mainBalance

    def debit(self, amount):
        if amount > self.MB:
            print("Insufficient funds")
            print("Available balance:", self.MB)
        else:
            self.MB -= amount
            print("Amount Debited")
            print("The total balance in the account is", self.MB)

    def credit(self, amount):
        self.MB += amount
        print("Amount Credited")
        print("The total balance in the account is", self.MB)


mainBalance = 1000000
acc = Account(mainBalance)

choice = int(input('Press 1 for debit and 2 for credit\n'))

if choice == 1:
    amount = int(input("Enter the amount to debit from your account\n"))
    acc.debit(amount)
elif choice == 2:
    amount = int(input("Enter the amount to credit into your account\n"))
    acc.credit(amount)
else:
    print("Invalid Input")