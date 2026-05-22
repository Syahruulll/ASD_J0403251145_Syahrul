class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.data, end=" ")
-
def preorderTraversal(root):
    if root:
        print(root.data, end=" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.data, end=" ")


# =====================
print("Nama : Syahrul Hidayatullah")
print("NIM  : J0403251145")

root = Node(45)

data = [25,65,15,35,55,75,30]

for i in data:
    insert(root,i)

print("\nIn-order Traversal:")
inorderTraversal(root)

print("\nPre-order Traversal:")
preorderTraversal(root)

print("\nPost-order Traversal:")
postorderTraversal(root)