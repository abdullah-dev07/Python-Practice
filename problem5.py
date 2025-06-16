class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        # i can add edge cases like setting a limit to the amount that can be deposited
        self.balance += amount
        print(f"deposit made of amount {amount}")


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"withdrawal made of amount {amount}. Remaining balance {self.balance}")
        else:
            print("insufficient balance :(")

    def display_balance(self):
        print(f"Available balance: {self.balance}")




account1 = BankAccount(123456, 5000)

account1.display_balance()

account1.deposit(500)

account1.withdraw(200)

account1.display_balance()