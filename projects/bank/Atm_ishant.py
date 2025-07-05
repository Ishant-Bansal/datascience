class Atm:
    def User(self, balance=50000, pin="9680"): 
        self.balance = balance
        self.pin = pin 

    def check_pin(self):
        attempts = 3
        while attempts>0:
         entered_pin = input("Enter your PIN: ")
         if entered_pin == self.pin:
            print("Authentication Successful\n")
            return True
         else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")
        print("Too many incorrect attempts. Exiting.")
        return False
            

    def check_balance(self):
        print(f"Your current balance is {self.balance}")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully!")
        else:
            print("Invalid deposit amount")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully!")
        else:
            print("Insufficient balance or invalid amount")
    def run(self):
        print("===== Welcome to ATM =====")
        if not self.check_pin():
            return

        while True:
            print("\n--- Menu ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Choose an option (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

atm = Atm()
atm.User() 
atm.run()