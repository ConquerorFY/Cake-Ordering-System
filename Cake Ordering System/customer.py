from file import *

class Customer:
    def __init__(self, custID, name, address, contact, username, password, left = None, right = None):
        self.custID = custID
        self.name = name
        self.address = address
        self.contact = contact
        self.username = username
        self.password = password
        self.left = left
        self.right = right

    # Getters
    def getCustID(self):
        return self.custID

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getContact(self):
        return self.contact

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    # Setters
    def setCustID(self, custID):
        self.custID = custID

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setContact(self, contact):
        self.contact = contact

    def setUsername(self, username):
        self.username = username

    def setPassword(self, password):
        self.password = password

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

class Auth:
    @staticmethod
    def authenticateCustomer(username, password):
        # authenticate and get result
        result = authenticateCustomerAccount(username, password)
        if result == 0:
            customerInfo = getCustomerDetailsByUsername(username)
            if customerInfo:
                createCustomerSessionFile(Customer(customerInfo[0], customerInfo[1], customerInfo[2], customerInfo[3], customerInfo[4], customerInfo[5]))
        return result

    @staticmethod   
    def registerCustomer(name, address, contact, username, password):
        # Generate new customer ID
        newCustID = getUniqueCustomerID()
        insertCustomerDataToFile(Customer(newCustID, name, address, contact, username, password))

    @staticmethod
    def getAuthenticatedCustomerDetails():
        custInfo = readCustomerSessionFile()
        return Customer(custInfo[0], custInfo[1], custInfo[2], custInfo[3], custInfo[4], custInfo[5])