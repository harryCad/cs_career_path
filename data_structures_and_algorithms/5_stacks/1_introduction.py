"""
Stacks Python Introduction
You have an understanding of how stacks work in theory, so now let’s see how they can be useful out in the wild — with Python!

Remember that there are three main methods that we want our stacks to have:

Push - adds data to the “top” of the stack
Pop - provides and removes data from the “top” of the stack
Peek - provides data from the “top” of the stack without removing it
We also need to consider the stack’s size and tweak our methods a bit so that our stack does not “overflow”.

Let’s get started building out our Stack class.

Instructions
1.
Within stack.py, create a Stack class.

Define an __init__() method for Stack. Inside the method, set an instance property top_item equal to None.


Stuck? Get a hint
2.
Below __init__(), define another method peek() that returns the value of the stack’s top_item using the Node method get_value().
"""

from node import Node

# Add your Stack class below:
class Stack:
    def __init__(self):
        self.top_item = None

    def peek(self):
        return self.top_item.get_value()