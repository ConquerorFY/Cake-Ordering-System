from utils import inorder

class Order:
    def __init__(self, orderID, cakeCode, quantity, custID, left = None, right = None):
        self.orderID = orderID
        self.cakeCode = cakeCode
        self.quantity = quantity
        self.custID = custID
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

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

class OrderBST:
    def __init__(self):
        self.root = None

    def add(self, orderID, cakeCode, quantity, custID):
        if not self.root:
            # if the BST is empty
            self.root = Order(orderID, cakeCode, quantity, custID)
        else:
            # insert based on cake code
            current = self.root

            while True:
                if orderID < current.getOrderID():
                    if not current.getLeft():
                        # insert at left leaf node
                        current.setLeft(Order(orderID, cakeCode, quantity, custID))
                        break
                    else:
                        # traverse down the left subtree
                        current = current.getLeft()

                elif orderID > current.getOrderID():
                    if not current.getRight():
                        # insert at right leaf node
                        current.setRight(Order(orderID, cakeCode, quantity, custID))
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

        node.left = self.constructPerfectBST(arr, start, mid - 1)
        node.right = self.constructPerfectBST(arr, mid + 1, end)

        return node

    def transformPerfectBST(self):
        # Inorder traversal to sort the nodes (based on customer ID)
        arr = []
        inorder(self.root, arr)
        n = len(arr)

        self.root = self.constructPerfectBST(arr, 0, n - 1)

    def update(self, orderID, cakeCode, quantity, custID):
        if not self.root:
            # if the BST is empty
            raise Exception
        else:
            # use breadth first search (BFS)
            queue = [self.root]

            while len(queue) > 0:
                current = queue.pop()

                if current.getOrderID() == orderID:
                    # update current node details
                    current.setCakeCode(cakeCode)
                    current.setQuantity(quantity)
                    current.setCustID(custID)
                    break

                if current.getLeft():
                    # if left node not None
                    queue.append(current.getLeft())

                if current.getRight():
                    # if right node not None
                    queue.append(current.getRight())

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