from utils import inorder
from file import *

class Order:
    def __init__(self, orderID, cakeCode, quantity, custID, status = "Pending", left = None, right = None):
        self.orderID = orderID
        self.cakeCode = cakeCode
        self.quantity = quantity
        self.custID = custID
        self.status = status
        self.left = left
        self.right = right

    # Getters
    def getOrderID(self):
        return self.orderID

    def getCakeCode(self):
        return self.cakeCode

    def getQuantity(self):
        return self.quantity

    def getCustID(self):
        return self.custID

    def getStatus(self):
        return self.status

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    # Setters
    def setOrderID(self, orderID):
        self.orderID = orderID

    def setCakeCode(self, cakeCode):
        self.cakeCode = cakeCode

    def setQuantity(self, quantity):
        self.quantity = quantity

    def setCustID(self, custID):
        self.custID = custID

    def setStatus(self, status):
        self.status = status

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

class OrderBST:
    def __init__(self):
        self.root = None

    def add(self, orderID, cakeCode, quantity, custID, status):
        if not self.root:
            # if the BST is empty
            self.root = Order(orderID, cakeCode, quantity, custID, status)
        else:
            # insert based on cake code
            current = self.root

            while True:
                if orderID < current.getOrderID():
                    if not current.getLeft():
                        # insert at left leaf node
                        current.setLeft(Order(orderID, cakeCode, quantity, custID, status))
                        break
                    else:
                        # traverse down the left subtree
                        current = current.getLeft()

                elif orderID > current.getOrderID():
                    if not current.getRight():
                        # insert at right leaf node
                        current.setRight(Order(orderID, cakeCode, quantity, custID, status))
                        break
                    else:
                        # traverse down the right subtree
                        current = current.getRight()

            self.transformPerfectBST()

    def constructPerfectBST(self, arr, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        node = arr[mid]

        node.setLeft(self.constructPerfectBST(arr, start, mid - 1))
        node.setRight(self.constructPerfectBST(arr, mid + 1, end))

        return node

    def transformPerfectBST(self):
        # Inorder traversal to sort the nodes (based on customer ID)
        arr = []
        inorder(self.root, arr)
        n = len(arr)

        self.root = self.constructPerfectBST(arr, 0, n - 1)

    def createNewOrder(self, cakeCode, quantity, custID):
        newOrderID = getUniqueOrderID()
        newOrder = Order(newOrderID, cakeCode, quantity, custID)
        insertOrderDataToFile(newOrder)
        self.getAllCustomerOrder()

    def getAllCustomerOrder(self):
        readCustomerOrderDataFromFile(self)

    def getSortedCustomerOrder(self):
        # Inorder traversal to get sorted order list (based on order ID)
        sortedOrderArr = []
        inorder(self.root, sortedOrderArr)

        return sortedOrderArr

    def modifyCustomerOrder(self, order):
        updateCustomerOrderDetails(order)
        readCustomerOrderDataFromFile(self)

    def print(self):
        if not self.root:
            raise Exception
        else:
            queue = [self.root]
            
            while len(queue) > 0:
                current = queue.pop()

                print(f"Order ID: {current.orderID}\nCakeCode: {current.cakeCode}\nQuantity: {current.quantity}\nCustomer ID: {current.custID}\n\n")

                if current.getLeft():
                    queue.insert(0, current.getLeft())

                if current.getRight():
                    queue.insert(0, current.getRight())