from cake import CakeBST
from order import OrderBST
from ui import *
from file import *

cakeBST = CakeBST()
orderBST = OrderBST()

def initSystem():
    readCakeDataFromFile(cakeBST)
    readOrderDataFromFile(orderBST)

def main():
    initSystem()
    welcomeScreen()

main()
