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
    def __init__(self, id, parent, children) -> None:
        self.id = id
        self.parent = None if not parent else parent
        self.children = [] if not children else children
