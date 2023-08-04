from os import system

balance = 1000
card_pin = 3211
login_attempts = 3
user_name = "User300"


def withdraw(): #Function to withdraw cash
    global balance
    
    withdraw_amount = int(input("Enter withdrawal amount: $"))
    
    if withdraw_amount > balance:
        print("Withdrawal amount is larger than current balance")
    else:
        balance -= withdraw_amount
        print(f"${withdraw_amount} have been successfully withdrawn from your account")
        print(f"Your Current Balance is ${balance}")
    
    return_or_exit = input("\nDo you want to return to main menu? Yes/No >> ").capitalize()
    
    if return_or_exit == "Yes":
        system("clear")
        menu()
    else:
        print("Thank you for using our ATM")
        exit()


def deposit(): #Function to deposit cash
    global balance
       
    deposit_amount = int(input("Enter amount of deposit: $"))
    balance += deposit_amount
    
    print(f"${deposit_amount} Have been successfully deposited to your account")
    print(f"Your current balance is ${balance}")
    
    return_or_exit = input("\nDo you want to return to main menu? Yes/No >> ").capitalize()
    
    if return_or_exit == "Yes":
        system("clear")
        menu()
    else:
        print("Thank you for using our ATM")
        exit()


def checkbalance(): #Function to check current balance
    global balance

    print(f"Your current balance is ${balance}")
    return_or_exit = input("\nDo you want to return to main menu? Yes/No >> ").capitalize()
    if return_or_exit == "Yes":
        system("clear")
        menu()
    else:
        print("Thank you for using our ATM")
        exit()


def changename(): #Function to change name
    login_attempts = 3
    global user_name
    
    print("Current Account Name: " + user_name)
    new_name = input("Enter new account name\n>> ")
    if new_name.isnumeric():
        system("clear")
        print("Account name cannot contain numbers only")
        changename()
    elif len(new_name) <= 4:
        system("clear")
        print("Account name must be over 4 characters long")
        changename()
    elif new_name[0].isnumeric():
        system("clear")
        print("First letter of account name should not be a number")
        changename()
    else:
        while login_attempts > 0:
            card_pin_prompt = int(input("Please confirm new name change with security PIN: "))
            if card_pin_prompt == card_pin:
                user_name = new_name
                print("Account name has been successfully updated")
                return_or_exit = input("\nDo you want to return to main menu? Yes/No >> ").capitalize()
                if return_or_exit == "Yes":
                    system("clear")
                    menu()
                else:
                    print("Thank you for using our ATM")
                    exit()
            else:
                login_attempts -= 1
                system("clear")
                print(f"Wrong PIN, {login_attempts} attempts left")
                if login_attempts == 0:
                    print("For security reasons your account has been locked. Please contact your nearest bank.")
                    exit()
            

def changepin(): #Function to change Security PIN
    login_attempts = 3
    global card_pin
    new_pin = input("Enter new security PIN: ")
    if new_pin.isnumeric():
        if len(new_pin) == 4:
            while login_attempts > 0:
                card_pin_prompt = int(input("Pleace confirm new PIN change with current card PIN: "))
                if card_pin_prompt == card_pin:
                    card_pin = int(new_pin)
                    print("Security PIN has been successfully updated")
                    return_or_exit = input("\nDo you want to go back to menu? Yes/No >> ").capitalize()
                    if return_or_exit == "Yes":
                        system("clear")
                        menu()
                    else:
                        print("Thank you for using our ATM")
                        exit()
                else:
                        login_attempts -= 1
                        system("clear")
                        print(f"Wrong PIN, {login_attempts} attempts left")
                        if login_attempts == 0:
                            print("For security reasons your account has been locked. Please contact your nearest bank.")
                            exit()
        else:
            system("clear")
            print("Security PIN must be a 4 digit number")
            changepin()
    else:
            system("clear")
            print("Security PIN must contain numbers only")
            changepin()
                
                
def menu():
    global user_name
    while True:
        system("clear")
        print("Account Name: " + user_name + "\n")
        prompt = input("""Choose an option:
------------------------------
1. Withdraw                  |
-----------------------------|
2. Deposit                   |
-----------------------------|
3. Check Balance             |
-----------------------------|
4. Change account name       |
-----------------------------|
5. Change Card Security PIN  |
-----------------------------|
0. Exit                      |
-----------------------------|
>> """)
        if prompt == "1":
            system("clear")
            withdraw()
        elif prompt == "2":
            system("clear")
            deposit()
        elif prompt == "3":
            system("clear")
            checkbalance()
        elif prompt == "4":
            system("clear")
            changename()
        elif prompt == "5":
            system("clear")
            changepin()
        elif prompt == "0":
                print("Thank you for using our ATM")
                exit()
        else:
            menu()
            


def login():
    global login_attempts
    while login_attempts > 0:
        card_pin_prompt = int(input("Please enter card security PIN: "))
        if card_pin_prompt == card_pin:
            menu()
        else:
            login_attempts -= 1
            system("clear")
            print(f"Wrong PIN, {login_attempts} attempts left")
            if login_attempts == 0:
                print("For security reasons your account has been locked. Please contact your nearest bank.")


system("clear")
print("===========================")
print("Welcome to Python Bank ATM")
print("===========================\n")


login()
