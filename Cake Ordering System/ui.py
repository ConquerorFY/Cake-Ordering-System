import re
from customer import Auth
from cake import CakeBST
from order import OrderBST

def welcomeScreen():
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
            loginScreen()
            return
        elif option == 2: 
            registerScreen()
            return
        elif option == 3:
            return

def loginScreen():
    while True:
        print("Login Screen")
        print("---------------------------------------------\n\n")

        username = input("Username: ")
        password = input("Password: ")

        print("\n\n1. Login")
        print("2. Return")
        option = int(input("Option: "))

        if option == 1:
            result = Auth.authenticateCustomer(username, password)
            if result == 0:
                print("\n\nAuthentication is successful!\n\n\n\n")
                # display customer dashboard after login success
                customerDashboard()
                return
            elif result == -1:
                print("\n\nInvalid password detected!\n\n\n\n")
            elif result == -2:
                print("\n\nCustomer account not found!\n\n\n\n")
            elif result == -3:
                print("\n\nAn error has occurred! Please try again!\n\n\n\n")
        elif option == 2:
            loginScreen()
            return

def registerScreen():
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
            Auth.registerCustomer(name, address, contact, username, password)
            print("\n\nRegistration is completed!!\n\n\n\n")
            welcomeScreen()
            return
        elif option == 2:
            print("\n\n\n\n")
            welcomeScreen()
            return

def customerDashboard():
    customerInfo = Auth.getAuthenticatedCustomerDetails()

    while True:
        print("Welcome back, " + customerInfo.getName())
        print("---------------------------------------------\n\n")

        print("Please select the operations you would like to do: ")
        print("1. View / Order Cakes")
        print("2. View / Modify Orders")
        print("3. Modify Account Details")
        print("4. Logout")
        option = int(input("Option: "))

        if option == 1:
            # view / order cakes
            return
        elif option == 2:
            # view / modify orders
            return
        elif option == 3:
            # modify account details
            customerUpdateScreen()
            return
        elif option == 4:
            # logout
            Auth.logOutCustomer()
            welcomeScreen()
            return

def customerUpdateScreen():
    while True:
        customerInfo = Auth.getAuthenticatedCustomerDetails()

        print("Update Customer Account Details")
        print("---------------------------------------------\n\n")

        print("Customer ID: " + customerInfo.getCustID())
        print("Name: " + customerInfo.getName())
        print("Address: " + customerInfo.getAddress())
        print("Contact: " + customerInfo.getContact())
        print("Username: " + customerInfo.getUsername())
        print("Password: " + re.sub(r'.', '*', customerInfo.getPassword()))

        print("\n\nPlease select an option: ")
        print("1. Update information")
        print("2. Return")
        option = int(input("Option: "))

        if option == 1:
            print("\n\n\n")
            while True:
                newName = input("Enter new name ('-' to skip): ")
                newAddress = input("Enter new address ('-' to skip): ")
                newContact = input("Enter new contact ('-' to skip): ")
                newUsername = input("Enter new username ('-' to skip): ")
                newPassword = input("Enter new password ('-' to skip): ")

                if newName != '-':
                    customerInfo.setName(newName)
                if newAddress != '-':
                    customerInfo.setAddress(newAddress)
                if newContact != '-':
                    customerInfo.setContact(newContact)
                if newUsername != '-':
                    customerInfo.setUsername(newUsername)
                if newPassword != '-':
                    customerInfo.setPassword(newPassword)

                Auth.updateCustomerAccount(customerInfo)
                print("Account details have been updated successfully!!\n\n")
                break

        elif option == 2:
            customerDashboard()
            return

def debugCakeBST(cakeBST: CakeBST):
    cakeBST.print()

def debugOrderBST(orderBST: OrderBST):
    orderBST.print()
