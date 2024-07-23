# New class written for solution
class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None


# New class written for solution
class DoublyLinkedList:

    def __init__(self):
        self.head, self.tail = Node(None, None), Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append_left(self, node):
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    def disconnect(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        self.list.disconnect(self.store[key])
        self.list.append_left(self.store[key])
        return self.store[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.list.disconnect(self.store[key])
        self.store[key] = Node(key, value)
        self.list.append_left(self.store[key])

        if len(self.store) > self.capacity:
            lru = self.list.tail.prev
            self.list.disconnect(lru)
            del self.store[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
#
# Design a data structure implementing a least-recently-used (LRU) cache
# i.e., when the number of keys exceeds the provisioned capacity, remove
# the least-recently-used key. 'get' and 'put' must run in O(1) time.
#
# Spec:
# - Cache has a capacity, cannot store more than that many keys
# - get(int key): returns the value of key if key exists, else -1
# - put(int key, int value): update value of key if key exists. Else add pair
#   to cache. If adding key would go over cache capacity, evict the
#   least-recently-used key first
# - ASSUME that on put, the newly inserted/updated key is the most-recently
#   used
#
# Solution:
# The cache needs O(1) access to get any item by its key. This has to be a
# map (dict).
#
# The cache ALSO needs an underlying collection that orders the items by access.
# Adding/updating/getting a key moves an item to the head of the collection,
# and all other items move down by 1. If the length of the collection exceeds
# capacity, the last item should be the least-recently-used.
#
# We need to be able to move any item to the start of the collection
# (most-recently-used) in O(1) time, from any other position. Removing the item
# from its original position must also take O(1). Only a LINKED LIST satisfies
# this requirement.
#
# We also need to be able to add items to the start of the list, and remove
# items from the end, in O(1) time. To remove from the end, we need to set
# the tail to the node before the tail in O(1). So we need a DOUBLY LIINKED
# LIST.
#
# Implement a DOUBLY LINKED LIST.
#
# Start with a ListNode class with key, val, prev and next fields.
#
# Then implement a doubly-linked list, either within LRUCache or in its own
# class.
#
# Use sentinel (dummy) nodes at the start and end, with key/val = None.
#
# Write methods for adding to the start of the list and removing from the end.
#
# Now for put, check if the value exists in the dict -- if yes, disconnect the
# node from its current position. Then add a new Node to the head of the list
# and update the dict with the new node.
#
# Finally, if the length of the dict is greater than capacity, remove the tail
# (node before the tail sentinel node, tail.prev).
#
# For get, check if the value exists in the dict -- if no, return -1. Otherwise
# disconnect the node from its current list position, add to the start of the
# list, and return its value.
