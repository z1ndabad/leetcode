
class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.mins:
            self.mins.append(val)
        else:
            self.mins.append(min(self.mins[-1], val))

        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
 
# Design a stack that supports push, pop, top, and retrieving the minimum
# element, all in O(1) time. getMin() does not remove elements from the stack.
#
# Intuition: on every push, the minimum element in the stack is either the
# current minimum element or the new element. On every pop, min element is
# the minimum at the time the new top element was inserted.
#
# Implement stack using a list. Either keep a separate list for the minimum
# element at the time each stack element was pushed, or store elements as
# tuples of (value, min). On push, check if the new element is smaller than
# the last min, and update the min value if yes. On pop, update the min value
# to the min attached to the new top of the stack.
