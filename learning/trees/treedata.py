class UnrootedTree:
    def __init__(self, graph=None) -> None:
        if graph is None:
            graph = {
                0: [1, 2, 5],
                1: [0],
                2: [0, 3],
                3: [2],
                5: [0, 4, 6],
                4: [5],
                6: [5],
            }
        self.graph = graph


class TreeNode:
    def __init__(self, id, parent=None, children=None) -> None:
        self.id = id
        self.parent = None if parent == None else parent
        self.children = [] if not children else children


class BinaryNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
