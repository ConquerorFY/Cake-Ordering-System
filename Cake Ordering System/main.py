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

def main():
    initSystem()
    debugCakeBST(cakeBST)

main()
