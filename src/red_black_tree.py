class Node:
    def __init__(self, key):
        pass

class RedBlackTree:
    def __init__(self):
        pass
    
    def search(self, key):
        """Return the node with the given key. If the key isn't on the tree, raise an exception."""
        pass

    def insert(self, key):
        """Insert a new node in the tree with the given key."""
        pass

    def remove(self, key):
        """Remove the node with the given key. If the key isn't on the tree, raise an exception."""
        pass

    def print(self):
        """Print the tree with a BFS traversal with node colors."""
        pass

def main():
    tree = RedBlackTree()
    tree.insert(10)
    tree.insert(7)
    tree.insert(16)
    tree.insert(15)
    tree.insert(18)
    tree.insert(30)
    tree.print()

    print(tree.search(15))

    tree.remove(15)

    print(tree.search(7))
    print(tree.search(15))

if __name__ == "__main__":
    main()
    
