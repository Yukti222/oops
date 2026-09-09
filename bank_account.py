class Acount:
    def __init__(self):
         self.bank_holder = " "
         self.__balance = 0.0

         self.menu()

    def menu(self):
        user_input = input (""" how would you like to proceed?
         1. enter 1 to deposit 
         2. enter 2 to withdraw
         3. enter 3 to check balance """)

        if user_input == "1":
           self.deposit()
        elif user_input == "2":
           self.withdraw()
        elif user_input == "3":
           print ("balance is : ", self.__balance )
        else :
          print ("bye ")


    def deposit(self):
            amount = float(input("enter the amount successfully"))
            if amount > 0:
               self.__balance += amount 
               print ("deposit successfull")
            else:
               print ("amount should be positive")


    def withdraw(self):
            amount = float(input("enter the amount to withdraw"))
            if amount > 0 and amount <= self.__balance:
                 self.balance -=amount 
            else :
                print ("insufficient balance ")



 
my_account = Acount()