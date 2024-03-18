class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def most_left(node):
    if not node.left:
        return node.value
    return most_left(node.left)


def searching_first_biggest(root, node):
    if node.right:
        return most_left(node.right)
    elif node == node.parent.left:
        return node.parent.value
    elif node.value < root.value:
        return root.value
    else:
        return node.value


root = Node(10)
root.left = Node(5)
root.left.parent = root
root.right = Node(15)
root.right.parent = root
root.left.right = Node(7)
root.left.right.parent = root.left
root.left.left = Node(3)
root.left.left.parent = root.left
root.right.right = Node(20)
root.right.right.parent = root.right
root.right.left = Node(12)
root.right.left.parent = root.right




node = root.right.right
print(searching_first_biggest(root, node))
