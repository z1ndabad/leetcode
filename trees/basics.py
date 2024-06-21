import copy


class Node:
    def __init__(self, value, children: list | None = None):
        self.value = value
        self.children = [] if not children else children

    def add_child(self, child):
        self.children.append(child)


def sum_leaves(node: Node):
    if not node:
        return 0

    if not node.children:
        return node.value

    sum = 0
    for child in node.children:
        sum += sum_leaves(child)

    return sum


def find_tree_height(node: Node):
    if not node:
        return -1

    if not node.children:
        return 0

    longest = 0
    for child in node.children:
        subtree_height = find_tree_height(child)
        if subtree_height > longest:
            longest = subtree_height

    return longest + 1


def find_tree_height_minimal(node: Node):
    longest = -1
    if not node:
        return longest

    for child in node.children:
        subtree_height = find_tree_height_minimal(child)
        if subtree_height > longest:
            longest = subtree_height

    return longest + 1


root_leaf_sum = Node(
    5,
    [
        Node(4, [Node(1, [Node(2), Node(9)]), Node(-6)]),
        Node(3, [Node(0), Node(7, [Node(8)]), Node(-4)]),
    ],
)

root_max_height = copy.deepcopy(root_leaf_sum)
root_max_height.add_child(Node(1, [Node(1, [Node(1, [Node(1, [Node(1)])])])]))

print(sum_leaves(root_leaf_sum))
print(find_tree_height(root_max_height))
print(find_tree_height_minimal(root_max_height))
