from linkedlistdata import ListNode
from typing import Optional


def merge_two_sorted_lists(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:

    # Important -- prevent inserting into an empty list by prepending the
    # output with a dummy node. Then it doesn't matter if list1 or list2
    # is None
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next

        tail = tail.next

    # Append whichever list is not exhausted (not None) to the output
    tail.next = list1 or list2

    return dummy.next


l1 = ListNode(-1, ListNode(0, ListNode(3, ListNode(5))))
l2 = ListNode(1, ListNode(2, ListNode(4, ListNode(6))))

print(merge_two_sorted_lists(l1, l2))
