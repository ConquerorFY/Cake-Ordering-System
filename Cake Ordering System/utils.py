import os

def inorder(current, arr):
    # Perform inorder traversal
    if current is None:
        return
    else:
        inorder(current.left, arr)
        arr.append(current)
        inorder(current.right, arr)

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')