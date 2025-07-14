from AtmMenu import show_menu
from AtmExceptions import DepositError, WithdrawError, InsufficientFundsError
from BankOperations import deposit, withdraw, check_balance

while True:
    show_menu()
    try:
        user_choice = int(input("Enter your choice: "))
        match user_choice:
            case 1:
                try:
                    deposit()
                except DepositError:
                    print("\tError: Deposit amount must be greater than zero.")
                except ValueError as e:
                    print(f"\tError: {e}")
            case 2:
                try:
                    withdraw()
                except WithdrawError:
                    print("\tError: Withdrawal amount must be greater than zero.")
                except InsufficientFundsError:
                    print("\tError: Insufficient funds. Maintain a minimum balance of INR 500.")
                except ValueError as e:
                    print(f"\tError: {e}")
            case 3:
                check_balance()
            case 4:
                print("Thank you for using this application!")
                break
            case _:
                print("Invalid selection. Please try again.")
    except ValueError:
        print("\tError: Please enter a valid numeric choice.")
