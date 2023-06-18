from utils import inorder
from file import insertCustomerDataToFile, readCustomerDataFromFile, createCustomerSessionFile, readCustomerSessionFile

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

class CustomerBST:
    def __init__(self):
        self.root = None

    def add(self, custID, name, address, contact, username, password):
        if not self.root:
            # if the BST is empty
            self.root = Customer(custID, name, address, contact, username, password)
        else:
            # insert based on customer ID
            current = self.root

            while True:
                if custID < current.getCustID():
                    if not current.getLeft():
                        # insert at left leaf node
                        current.setLeft(Customer(custID, name, address, contact, username, password))
                        break
                    else:
                        # traverse down the left subtree
                        current = current.getLeft()

                elif custID > current.getCustID():
                    if not current.getRight():
                        # insert at right leaf node
                        current.setRight(Customer(custID, name, address, contact, username, password))
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

    def update(self, custID, name, address, contact, username, password):
        if not self.root:
            # if the BST is empty
            raise Exception
        else:
            # use breadth first search (BFS)
            queue = [self.root]

            while len(queue) > 0:
                current = queue.pop()

                if current.getCustID() == custID:
                    # update current node details
                    current.setName(name)
                    current.setAddress(address)
                    current.setContact(contact)
                    current.setUsername(username)
                    current.setPassword(password)
                    break

                if current.getLeft():
                    # if left node not None
                    queue.append(current.getLeft())

                if current.getRight():
                    # if right node not None
                    queue.append(current.getRight())

    def authenticateCustomer(self, username, password):
        if not self.root:
            return -1 # No user account exists
        else:
            queue = [self.root]

            while len(queue) > 0:
                current = queue.pop()

                if current.getUsername() == username:
                    if current.getPassword() == password:
                        # Create logged in session file for customer
                        createCustomerSessionFile(current)
                        return 0 # Authentication success
                    else:
                        return -2 # Invalid password

                if current.getLeft():
                    queue.insert(0, current.getLeft())

                if current.getRight():
                    queue.insert(0, current.getRight())

            return -1

    def getAuthenticatedCustomerDetails(self):
        customer = readCustomerSessionFile()

        if not customer:
            raise Exception("Please login first before invoking this function!")

        return Customer(customer[0], customer[1], customer[2], customer[3], customer[4], customer[5])

    def registerCustomer(self, name, address, contact, username, password):
        # Generate new customer ID
        arr = []
        inorder(self.root, arr)
        newCustID = int(max([node.getCustID() for node in arr])) + 1 if len(arr) > 0 else 1

        insertCustomerDataToFile(Customer(newCustID, name, address, contact, username, password))
        readCustomerDataFromFile(self)

    def print(self):
        if not self.root:
            raise Exception
        else:
            queue = [self.root]
            
            while len(queue) > 0:
                current = queue.pop()

                print(f"Customer ID: {current.custID}\nName: {current.name}\nAddress: {current.address}\nContact: {current.contact}\n\n")

                if current.getLeft():
                    queue.insert(0, current.getLeft())

                if current.getRight():
                    queue.insert(0, current.getRight())