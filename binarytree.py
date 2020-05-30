class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def inorder(self):
        traversal = []
        if self.left:
            traversal += self.left.inorder()
        traversal.append(self.data)
        if self.right:
            traversal += self.right.inorder()
        return traversal

    def postorder(self):
        visited = []
        if self.left:
            visited += self.left.postorder()
        if self.right:
            visited += self.right.postorder()
        visited.append(self.data)
        return visited


class BinaryTree:

    def __init__(self, r):
        self.root = r

    def inorder(self):
        if self.root:
            return self.root.inorder()
        else:
            return []

    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []
