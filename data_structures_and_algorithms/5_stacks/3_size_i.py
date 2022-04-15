"""
Stacks Python Size I
With stacks, size matters. If we’re not careful, we can accidentally over-fill them with data. Since we don’t want any stack overflow, we need to go back and make a few modifications to our methods that help us track and limit the stack size so we can keep our stacks healthy.

What do we do if someone tries to peek() or pop() when our stack is empty?

How do we keep someone from push()ing to a stack that has already reached its limit?

How do we even know how large our stack has gotten?

Instructions
1.
In __init__(), let’s add two new properties: size and limit.

limit should be accepted as a parameter with a default of 1000. Inside the method, set the instance limit property to the passed in value of limit.

size should be set to 0 in __init__().

2.
In peek() and pop(), wrap the current body of each method in an if clause that checks if the size of the stack is greater than 0.

At the end of each method, outside the if clause, add an else clause with a print statement to let users know that the stack is empty.

3.
In pop() just before the return statement, reduce the size of the stack by 1.
"""

from node import Node

class Stack:
    def __init__(self, limit=1000):
        self.top_item = None
        self.size = 0
        self.limit = limit

    def push(self, value):
        item = Node(value)
        item.set_next_node(self.top_item)
        self.top_item = item

    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            # Decrement the stack size here:
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Stack is empty!")

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()
        else:
            print("Stack is empty!")