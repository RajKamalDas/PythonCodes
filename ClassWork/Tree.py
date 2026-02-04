class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
        else:
            print("\nIt already exists!")

    def inOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.inOrderTraversal()

        elements.append(self.val)
        
        if self.right:
            elements += self.right.inOrderTraversal()
        return elements


tree = TreeNode(5)
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(10)

print(tree.inOrderTraversal())
