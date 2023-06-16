from customer import *
from cake import *
from order import *
from ui import *
from file import *

customerBST = CustomerBST()
cakeBST = CakeBST()
orderBST = OrderBST()

def initSystem():
    readCakeDataFromFile(cakeBST)
    readCustomerDataFromFile(customerBST)
    readOrderDataFromFile(orderBST)

def main():
    initSystem()
    welcomeScreen(customerBST)

main()
