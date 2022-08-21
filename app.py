"""
ATM BANKING APP
by Randall Tr
April 30, 2022
"""


from banking_pkg import account

# Prints ATM Menu
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("\n          === Automated Teller Machine ===          ")

# Collects name of new user
while True:
    name = input("Enter name to register: ").strip().title()
    if len(name) < 1 or len(name) > 10:
        print("The maximum name length is 10 characters.")
        continue
    else:
        break

# Collects PIN of new user
while True:
    pin = input("Enter PIN: ")
    if len(pin) != 4:
        print("PIN must contain 4 numbers.")
    else:
        break

# Initializes balance
balance = 0
print(f"{name} has been registered with a starting balance of ${str(balance)}")

# Validates name and PIN of user
while True:
    print("\nLOGIN")
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name_to_validate.lower() == name.lower() and pin_to_validate == pin:
        print("Login successful!")
        break
    else:
        print("Invalid credentials")
        continue

# Logic for ATM menu
while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdrawal(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
    else:
        print("Invalid selection. Try again.")
