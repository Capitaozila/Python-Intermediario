class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class ArvoreBinaria:
    def __init__(self, data=None):
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def in_ordem(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end="")
            self.in_ordem(node.left)
        print(node, end="")
        if node.right:
            self.in_ordem(node.right)
            print(')', end="")


if __name__ == "__main__":
    """tree = ArvoreBinaria(7)
    tree.root.left = Node(18)
    tree.root.right = Node(14)
    print(tree.root)
    print(tree.root.right)
    print(tree.root.left)"""

    tree = ArvoreBinaria()
    n1 = Node("A")
    n2 = Node("+")
    n3 = Node("*")
    n4 = Node("B")
    n5 = Node("-")
    n6 = Node("/")
    n7 = Node("C")
    n8 = Node("D")
    n9 = Node("E")

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3

    tree.root = n2
    tree.in_ordem()
