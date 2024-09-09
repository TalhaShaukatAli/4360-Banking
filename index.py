def show_balance(balance):
    print("*********************")
    print(f"Your balance is ${balance:.2f}")
    print("*********************")

def deposit():
    print("*********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("*********************")
    if amount < 0:
        print("*********************")
        print("That's not a valid amount")
        print("*********************")
        return 0
    else:
        print("*********************")
        print("Amount successfully deposited")
        print("*********************")
        return amount

def withdraw(balance):
    print("*********************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("*********************")

    if amount > balance:
        print("*********************")
        print("Insufficient funds")
        print("*********************")
        return 0
    elif amount < 0:
        print("*********************")
        print("Amount must be greater than 0")
        print("*********************")
        return 0
    else:
        print("*********************")
        print("Amount successfully withdrawn")
        print("*********************")
        return amount
    
def transfer(balance):
    print("*********************")
    amount = float(input("Enter the amount to be transferred: "))
    print("*********************")

    if amount > balance:
        print("*********************")
        print("Insufficient funds")
        print("*********************")
        return 0
    elif amount < 1:
        print("*********************")
        print("Amount must be greater than 0")
        print("*********************")
        return 0
    elif amount > 10000:
        print("*********************")
        print("Transfer limit exceeded. Please try again.")
        print("*********************")
        return 0
    else:
        print("*********************")
        print("Amount successfully transferred")
        print("*********************")
        return amount
    
def sign_in():
    print("*****************************")
    print(" Welcome to the Banking App! ")
    print("     Please Sign In ")
    print("*****************************")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("*********************")


    if username == "justin" and password == "software":
        print("Sign-in successful!")
        return True
    else:
        print("Invalid username or password.")
        return False
    
def lock_account():
    print("*********************")
    print("Account locked")
    print("*********************")
    exit()

def account_options():
    print("*********************")
    print("Which account would you like to use?")
    print("1. Account 1")
    print("2. Account 2")
    print("3. Exit")
    print("*********************")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        return 1
    elif choice == '2':
        return 2
    elif choice == '3':
        print("Have a nice day!")
        exit()
    else:
        print("Invalid choice. Exiting program.")
        exit()

def main():
    if not sign_in():
        print("Access denied. Exiting program.")
        exit()

    account = account_options()

    balance_1 = 0
    balance_2 = 0
    is_running = True

    while is_running:
        balance = balance_1 if account == 1 else balance_2

        print("*********************")
        print(f" Banking App - Account {account} ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Lock Account")
        print("6. Exit")
        print("*********************")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            if account == 1:
                balance_1 += deposit()
            else:
                balance_2 += deposit()
        elif choice == '3':
            if account == 1:
                balance_1 -= withdraw(balance_1)
            else:
                balance_2 -= withdraw(balance_2)
        elif choice == '4':
            if account == 1:
                balance_1 -= transfer(balance_1)
            else:
                balance_2 -= transfer(balance_2)
        elif choice == '5':
            lock_account()
        elif choice == '6':
            is_running = False
        else:
            print("*********************")
            print("That is not a valid choice")
            print("*********************")

    print("*********************")
    print("Thank you! Have a nice day!")
    print("*********************")

if __name__ == '__main__':
    main()
