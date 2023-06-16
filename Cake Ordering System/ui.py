from customer import CustomerBST
from cake import CakeBST
from order import OrderBST

def welcomeScreen(customerBST: CustomerBST):
    while True:
        print("   _____          _  ________    ____  _____  _____  ______ _____  _____ _   _  _____    _______     _______ _______ ______ __  __ ")
        print("  / ____|   /\   | |/ /  ____|  / __ \|  __ \|  __ \|  ____|  __ \|_   _| \ | |/ ____|  / ____\ \   / / ____|__   __|  ____|  \/  |")
        print(" | |       /  \  | ' /| |__    | |  | | |__) | |  | | |__  | |__) | | | |  \| | |  __  | (___  \ \_/ / (___    | |  | |__  | \  / |")
        print(" | |      / /\ \ |  < |  __|   | |  | |  _  /| |  | |  __| |  _  /  | | | . ` | | |_ |  \___ \  \   / \___ \   | |  |  __| | |\/| |")
        print(" | |____ / ____ \| . \| |____  | |__| | | \ \| |__| | |____| | \ \ _| |_| |\  | |__| |  ____) |  | |  ____) |  | |  | |____| |  | |")
        print("  \_____/_/    \_\_|\_\______|  \____/|_|  \_\_____/|______|_|  \_\_____|_| \_|\_____| |_____/   |_| |_____/   |_|  |______|_|  |_|\n\n\n")

        print("Please select an option: ")
        print("1. Login as customer")
        print("2. Register new customer account")
        print("3. Exit\n\n")

        option = int(input("Option: "))
        if option == 1: 
            loginScreen(customerBST)
            return
        elif option == 2: 
            registerScreen(customerBST)
            return
        elif option == 3:
            return

def loginScreen(customerBST: CustomerBST):
    while True:
        print("Login Screen")
        print("---------------------------------------------\n\n")

        username = input("Username: ")
        password = input("Password: ")

        print("\n\n1. Login")
        print("2. Return")
        option = int(input("Option: "))

        if option == 1:
            result = customerBST.authenticateCustomer(username, password)
            if result == 0:
                print("\n\nAuthentication is successful!\n\n\n\n")
                # handle after login functions
                return
            elif result == -1:
                print("\n\nNo user account exists!\n\n\n\n")
            elif result == -2:
                print("\n\nInvalid password detected!\n\n\n\n")
        elif option == 2:
            loginScreen(customerBST)
            return

def registerScreen(customerBST: CustomerBST):
    while True:
        print("Register Screen")
        print("---------------------------------------------\n\n")

        name = input("Customer Name: ")
        address = input("Address: ")
        contact = input("Contact: ")
        username = input("Username: ")
        password = input("Password: ")

        print("\n\n1. Submit Information")
        print("2. Return")
        option = int(input("Option: "))

        if option == 1:
            customerBST.registerCustomer(name, address, contact, username, password)
            print("\n\nRegistration is completed!!\n\n\n\n")
            welcomeScreen(customerBST)
            return
        elif option == 2:
            print("\n\n\n\n")
            welcomeScreen(customerBST)
            return

def debugCustomerBST(customerBST: CustomerBST):
    customerBST.print()

def debugCakeBST(cakeBST: CakeBST):
    cakeBST.print()

def debugOrderBST(orderBST: OrderBST):
    orderBST.print()
