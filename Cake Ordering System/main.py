from customer import CustomerBST
from cake import CakeBST
from order import OrderBST
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
