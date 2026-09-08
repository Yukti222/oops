class ATM:
    # Called automatically when an ATM object is created.
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input(
            """How would you like to proceed?
1. Enter 1 to create a pin
2. Enter 2 to deposit
3. Enter 3 to withdraw
4. Enter 4 to check balance
5. Enter 5 to exit
"""
        )

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Bye")
        else:
            print("Invalid choice")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("PIN created successfully")

    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            if amount > 0:
                self.balance += amount
                print("Deposit successful")
            else:
                print("Amount must be positive")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the amount: "))
            if 0 < amount <= self.balance:
                self.balance -= amount
                print("Operation successful")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("Invalid pin")


ATM()
