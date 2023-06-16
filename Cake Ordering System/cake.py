from utils import inorder

class Cake:
    def __init__(self, cakeCode, flavor, weight, unitPrice, left = None, right = None):
        self.cakeCode = cakeCode
        self.flavor = flavor
        self.weight = weight
        self.unitPrice = unitPrice
        self.left = left
        self.right = right

    # Getters
    def getCakeCode(self):
        return self.cakeCode

    def getFlavor(self):
        return self.flavor

    def getWeight(self):
        return self.weight

    def getUnitPrice(self):
        return self.unitPrice

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    # Setters
    def setCakeCode(self, cakeCode):
        self.cakeCode = cakeCode

    def setFlavor(self, flavor):
        self.flavor = flavor

    def setWeight(self, weight):
        self.weight = weight

    def setUnitPrice(self, unitPrice):
        self.unitPrice = unitPrice

    def setLeft(self, left):
        self.left = left

    def setRight(self, right):
        self.right = right

class CakeBST:
    def __init__(self):
        self.root = None

    def add(self,  cakeCode, flavor, weight, unitPrice):
        if not self.root:
            # if the BST is empty
            self.root = Cake(cakeCode, flavor, weight, unitPrice)
        else:
            # insert based on cake code
            current = self.root

            while True:
                if cakeCode < current.getCakeCode():
                    if not current.getLeft():
                        # insert at left leaf node
                        current.setLeft(Cake(cakeCode, flavor, weight, unitPrice))
                        break
                    else:
                        # traverse down the left subtree
                        current = current.getLeft()

                elif cakeCode > current.getCakeCode():
                    if not current.getRight():
                        # insert at right leaf node
                        current.setRight(Cake(cakeCode, flavor, weight, unitPrice))
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
        # Inorder traversal to sort the nodes (based on cake code)
        arr = []
        inorder(self.root, arr)
        n = len(arr)

        # Reassign transformed root to self.root
        self.root = self.constructPerfectBST(arr, 0, n - 1)

    def update(self, cakeCode, flavor, weight, unitPrice):
        if not self.root:
            # if the BST is empty
            raise Exception
        else:
            # use breadth first search (BFS)
            queue = [self.root]

            while len(queue) > 0:
                current = queue.pop()

                if current.getCakeCode() == cakeCode:
                    # update current node details
                    current.setFlavor(flavor)
                    current.setWeight(weight)
                    current.setUnitPrice(unitPrice)
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

                print(f"Cake Code: {current.cakeCode}\nFlavor: {current.flavor}\nWeight: {current.weight}\nUnit Price: {current.unitPrice}\n\n")

                if current.getLeft():
                    queue.insert(0, current.getLeft())

                if current.getRight():
                    queue.insert(0, current.getRight())