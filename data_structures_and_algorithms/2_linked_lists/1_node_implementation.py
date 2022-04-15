"""
Node Implementation
Let’s implement a linked list in Python. As you might recall, each linked list is a sequential chain of nodes.
So before we start building out the LinkedList itself, we want to build up a Node class in Python that we can use to build our data containers.

Remember that a node contains two elements:

data
a link to the next node
Ready? Let’s get started!

Note: Because the workspace is set up with spaces instead of tabs, you will need to use spaces to prevent Python from throwing an error.
You can learn more about this here.

Instructions
1.
Within script.py in the pane to the right, create an empty Node class.

Inside, define an __init__() method for the Node. It should take a value and a next_node.

next_node should default to None if not provided. These variables should be saved to self with corresponding key names.

Checkpoint 2 Passed

Stuck? Get a hint
2.
Define .get_value() and .get_next_node() methods. These should return the corresponding values from self.

Checkpoint 3 Passed

Stuck? Get a hint
3.
Define a .set_next_node() method that takes self and next_node as parameters and allows you to update the link to the next node.

Checkpoint 4 Passed

Stuck? Get a hint
4.
Outside the Node class, create an instance of Node called my_node with a value of 44.

Use .get_value() to print the value of my_node.
"""

# Define your Node class below:
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value
  def get_next_node(self):
    return self.next_node

  def set_next_node(self, next_node):
    self.next_node = next_node

my_node = Node(44)
print(my_node.get_value())