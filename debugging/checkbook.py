class Checkbook:
    """
    A class representing a simple checkbook.

    Attributes:
    - balance: A float representing the current balance in the checkbook.
    """

    def __init__(self):
        """
        Initializes the checkbook with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits the specified amount into the checkbook.

        Parameters:
        - amount: A float representing the amount to be deposited.
        """
        try:
            amount = float(amount)
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the checkbook if sufficient funds are available.

        Parameters:
        - amount: A float representing the amount to be withdrawn.
        """
        try:
            amount = float(amount)
            if amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    def get_balance(self):
        """
        Displays the current balance in the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the checkbook.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
