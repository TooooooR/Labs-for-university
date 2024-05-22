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
