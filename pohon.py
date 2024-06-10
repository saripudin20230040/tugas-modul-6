class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)
    
    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.val)
            self.inorder_traversal(node.right, result)
        return result

    def preorder_traversal(self, node, result):
        if node:
            result.append(node.val)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        return result

    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.val)
        return result

# Contoh penggunaan
if __name__ == "__main__":
    tree = BinaryTree()
    elements = [5, 3, 7, 2, 4, 6, 8]

    for elem in elements:
        tree.insert(elem)
    
    print("Inorder traversal:", tree.inorder_traversal(tree.root, []))
    print("Preorder traversal:", tree.preorder_traversal(tree.root, []))
    print("Postorder traversal:", tree.postorder_traversal(tree.root, []))
