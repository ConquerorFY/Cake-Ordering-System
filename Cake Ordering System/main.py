from cake import CakeBST
from order import OrderBST
from ui import *
from file import *

cakeBST = CakeBST()
orderBST = OrderBST()

def initSystem():
    readAllCakeDataFromFile(cakeBST)

def main():
    initSystem()
    welcomeScreen(cakeBST, orderBST)

main()
