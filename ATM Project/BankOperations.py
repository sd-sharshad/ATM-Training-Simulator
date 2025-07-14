#Run the Main Driver File i.e AtmOperationDemo.py
#BankOperations.py
from AtmExceptions import WithdrawError, InsufficientFundsError, DepositError

account_balance = 500.00  # Starting balance

def deposit():
    try:
        deposit_amount = float(input("Enter your deposit amount: "))
        if deposit_amount <= 0:
            raise DepositError
        else:
            global account_balance
            account_balance += deposit_amount
            print(f"\tYour Account xxxxxxxx123 credited with INR: {deposit_amount}")
            print(f"\tCurrent available balance in xxxxxxxx123 is INR: {account_balance}")
    except ValueError:
        raise ValueError("Invalid input: Please enter a numeric deposit amount.")

def withdraw():
    try:
        withdrawal_amount = float(input("Enter your withdrawal amount: "))
        global account_balance
        if withdrawal_amount <= 0:
            raise WithdrawError
        elif (withdrawal_amount + 500) > account_balance:
            raise InsufficientFundsError
        else:
            account_balance -= withdrawal_amount
            print(f"\tYour Account xxxxxxxx123 debited with INR: {withdrawal_amount}")
            print(f"\tCurrent available balance in xxxxxxxx123 is INR: {account_balance}")
    except ValueError:
        raise ValueError("Invalid input: Please enter a numeric withdrawal amount.")

def check_balance():
    print(f"\tAvailable balance in your xxxxxxxx123 is INR: {account_balance}")
