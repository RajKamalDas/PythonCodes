class NaryTree:
    def __init__(self, data):
        self.data = data
        self.children = []

    def addChild(self, childNode):
        self.children.append(childNode)

    def preOrderTraversal(self):
        elements = [self.data]
        for child in self.children:
            elements += child.preOrderTraversal()
        return elements
