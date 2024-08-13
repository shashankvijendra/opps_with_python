class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient funds or amount cannot be negative.")

    def get_balance(self):
        return self.__balance

    def display_account_details(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Balance: ${self.__balance}")



# Creating a new bank account
my_account = BankAccount(account_number="123456789")

# Depositing money
my_account.deposit(100)

# Withdrawing money
my_account.withdraw(50)

# Checking the balance
print(my_account.get_balance())

# Displaying account details
my_account.display_account_details()
