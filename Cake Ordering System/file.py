import os

cakeFile = "cake.txt"
customerFile = "customer.txt"
orderFile = "order.txt"
sessionFile = "session.txt"
separator = "||"

def readCakeDataFromFile(cakeBST):
    cakeBST.root = None
    try:
        file = open(cakeFile, "r")

        for line in file:
            data = line.split(separator)
            cakeCode = data[0]
            flavor = data[1]
            weight = data[2]
            unitPrice = data[3]
            cakeBST.add(cakeCode, flavor, weight, unitPrice)

        file.close()

    except FileNotFoundError:
        with open(cakeFile, "w") as file:
            file.write("")

def readCustomerDataFromFile(customerBST):
    customerBST.root = None
    try:
        file = open(customerFile, "r")

        for line in file:
            data = line.split(separator)
            custID = data[0]
            name = data[1]
            address = data[2]
            contact = data[3]
            username = data[4]
            password = data[5]
            customerBST.add(custID, name, address, contact, username, password)

        file.close()

    except FileNotFoundError:
        with open(customerFile, "w") as file:
            file.write("")

def readOrderDataFromFile(orderBST):
    orderBST.root = None
    try:
        file = open(orderFile, "r")

        for line in file:
            data = line.split(separator)
            orderID = data[0]
            cakeCode = data[1]
            quantity = data[2]
            custID = data[3]
            orderBST.add(orderID, cakeCode, quantity, custID)

        file.close()

    except FileNotFoundError:
        with open(orderFile, "w") as file:
            file.write("")

def insertCustomerDataToFile(customer):
    with open(customerFile, 'a') as file:
        file.write(str(customer.getCustID()) + separator + customer.getName() + separator + customer.getAddress() + separator + customer.getContact() + separator + customer.getUsername() + separator + customer.getPassword() + separator + "\n")

def insertOrderDataToFile(order):
    with open(orderFile, 'a') as file:
        file.write(str(order.getOrderID()) + separator + str(order.getCustID()) + separator + str(order.getQuantity()) + separator + str(order.getCustID()) + separator + "\n")

def createCustomerSessionFile(customer):
    with open(sessionFile, 'w') as file:
        file.write(str(customer.getCustID()) + separator + customer.getName() + separator + customer.getAddress() + separator + customer.getContact() + separator + customer.getUsername() + separator + customer.getPassword() + separator)

def readCustomerSessionFile():
    try:
        file = open(sessionFile, "r")

        for line in file:
            data = line.split(separator)
            custID = data[0]
            name = data[1]
            address = data[2]
            contact = data[3]
            username = data[4]
            password = data[5]

            file.close()
            return [custID, name, address, contact, username, password]

    except FileNotFoundError:
        print("Session file not created! Customer have not login!")
        return None

def clearCustomerSessionFile():
    if os.path.exists(sessionFile):
        os.remove(sessionFile)