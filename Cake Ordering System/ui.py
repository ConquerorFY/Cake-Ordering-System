import re
from customer import Auth
from cake import Cake, CakeBST
from order import Order, OrderBST

def welcomeScreen(cakeBST: CakeBST, orderBST: OrderBST):
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
            loginScreen(cakeBST, orderBST)
            return
        elif option == 2: 
            registerScreen()
            return
        elif option == 3:
            return

def loginScreen(cakeBST: CakeBST, orderBST: OrderBST):
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
                orderBST.getAllCustomerOrder()
                # display customer dashboard after login success
                customerDashboard(cakeBST, orderBST)
                return
            elif result == -1:
                print("\n\nInvalid password detected!\n\n\n\n")
            elif result == -2:
                print("\n\nCustomer account not found!\n\n\n\n")
            elif result == -3:
                print("\n\nAn error has occurred! Please try again!\n\n\n\n")
        elif option == 2:
            loginScreen(cakeBST, orderBST)
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

def customerDashboard(cakeBST: CakeBST, orderBST: OrderBST):
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
            cakeDisplayOrderingScreen(cakeBST, orderBST)
            return
        elif option == 2:
            # view / modify orders
            orderViewUpdateScreen(cakeBST, orderBST)
            return
        elif option == 3:
            # modify account details
            customerUpdateScreen()
            return
        elif option == 4:
            # logout
            Auth.logOutCustomer()
            welcomeScreen(cakeBST, orderBST)
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

def cakeDisplayOrderingScreen(cakeBST: CakeBST, orderBST: OrderBST):
    custID = Auth.getAuthenticatedCustomerDetails().getCustID()
    cakeList = cakeBST.getSortedCakeList()
    currentCakeIndex = 0
    lastCakeIndex = len(cakeList) - 1

    while True:
        print("Cake Shop Ordering Screen")
        print("---------------------------------------------\n\n")

        currentCake: Cake = cakeList[currentCakeIndex]
        print("Cake Code: " + str(currentCake.getCakeCode()))
        print("Cake Flavour: " + currentCake.getFlavor())
        print("Cake Weight: " + str(currentCake.getWeight()))
        print("Cake Unit Price: " + str(currentCake.getUnitPrice()))

        print("\n\n---------------------------------------------")
        print("[R]eturn    [P]revious     [O]rder     [N]ext")
        print("---------------------------------------------")
        
        option = input()
        if option == 'P' or option == 'p':
            # Previous cake
            if currentCakeIndex > 0:
                currentCakeIndex -= 1
        elif option == 'N' or option == 'n':
            # Next cake
            if currentCakeIndex < lastCakeIndex:
                currentCakeIndex += 1
        elif option == 'O' or option == 'o':
            # Order cake
            while True:
                cakeAmount = int(input("How many cake would you like to order? "))
                print("---------------------------------------------")
                print("         Order             Confirmation      ")
                print("---------------------------------------------\n\n")

                print("Cake Code: " + str(currentCake.getCakeCode()))
                print("Cake Flavour: " + currentCake.getFlavor())
                print("Cake Weight: " + str(currentCake.getWeight()))
                print("Quantity: " + str(cakeAmount))
                print("Total Price: " + "RM" + "{:.2f}".format(float(currentCake.getUnitPrice()[2:]) * cakeAmount))

                confirmation = input("Confirm ? (Y)")
                if confirmation == 'Y' or confirmation == 'y':
                    # Add new order
                    orderBST.createNewOrder(currentCake.getCakeCode(), cakeAmount, custID)
                    print("A new order has been created!")
                    break
                else:
                    break
        elif option == 'R' or option == 'r':
            customerDashboard(cakeBST, orderBST)
            return

def orderViewUpdateScreen(cakeBST: CakeBST, orderBST: OrderBST):
    cakeList = cakeBST.getSortedCakeList()
    currentOrderIndex = 0

    while True:
        orderList = orderBST.getSortedCustomerOrder()
        lastOrderIndex = len(orderList) - 1

        print("Cake Shop Order History & Modification Screen")
        print("-----------------------------------------------------------\n\n")

        currentOrder: Order = orderList[currentOrderIndex]
        currentCake: Cake = list(filter(lambda cake: cake.getCakeCode() == currentOrder.getCakeCode(), cakeList))[0]

        print("Order ID: " + str(currentOrder.getOrderID()))
        print("Cake Code: " + str(currentCake.getCakeCode()))
        print("Cake Flavour: " + currentCake.getFlavor())
        print("Cake Weight: " + str(currentCake.getWeight()))
        print("Cake Unit Price: " + str(currentCake.getUnitPrice()))
        print("Cake Quantity: " + str(currentOrder.getQuantity()))
        print("Total Price: " + "RM" + "{:.2f}".format(float(currentCake.getUnitPrice()[2:]) * int(currentOrder.getQuantity())))
        print("Order Status: " + currentOrder.getStatus())

        print("\n\n---------------------------------------------")
        print("[R]eturn   [P]revious     [M]odify     [N]ext")
        print("---------------------------------------------")

        option = input()
        if option == 'P' or option == 'p':
            # Previous order
            if currentOrderIndex > 0:
                currentOrderIndex -= 1
        elif option == 'N' or option == 'n':
            # Next order
            if currentOrderIndex < lastOrderIndex:
                currentOrderIndex += 1
        elif option == 'M' or option == 'm':
            # Modify order status
            newOrderStatus = input("What is the new status of the order? ('-' to skip) ")
            currentOrder.setStatus(newOrderStatus)
            orderBST.modifyCustomerOrder(currentOrder)
            print("Order have been updated!")
        elif option == 'R' or option == 'r':
            customerDashboard(cakeBST, orderBST)
            return

def debugCakeBST(cakeBST: CakeBST):
    cakeBST.print()

def debugOrderBST(orderBST: OrderBST):
    orderBST.print()
