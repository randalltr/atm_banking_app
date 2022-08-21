def show_balance(balance):
    print(f"Current balance: ${str(balance)}")


def deposit(balance):
    amount = int(input("Enter amount to deposit: "))
    return balance + amount


def withdrawal(balance):
    amount = int(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Where are you going to get that kind of money?")
        return balance
    else:
        return balance - amount


def logout(name):
    print(f"Goodbye {name}!")
