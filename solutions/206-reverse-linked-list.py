class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node = head
        prev = None

        while node is not None:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node

        return prev
