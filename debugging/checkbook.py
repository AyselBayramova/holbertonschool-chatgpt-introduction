#!/usr/bin/python3

class Checkbook:
    """
    A simple Checkbook class to manage bank account operations
    such as deposit, withdrawal, and checking balance.
    """

    def __init__(self):
        # Initialize account balance to 0.0
        self.balance = 0.0

    def deposit(self, amount):
        """
        Add money to the account balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient balance exists.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display current account balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main program loop that interacts with the user.
    Provides options: deposit, withdraw, balance, exit.
    """
    cb = Checkbook()

    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")

        if action.lower() == 'exit':
            break

        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)

        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)

        elif action.lower() == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
