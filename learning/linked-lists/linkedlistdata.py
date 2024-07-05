class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = []
        node = self
        while node:
            res.append(node.val)
            node = node.next
        return str(res)
