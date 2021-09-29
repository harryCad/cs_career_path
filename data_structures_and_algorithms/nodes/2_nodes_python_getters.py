"""
Nodes Python Getters
We need methods to access the data and link within the node. For this, we will use two getters, .get_value() and .get_link_node().

These should each return their corresponding value on the self object.

Instructions
1.
Implement the .get_value() getter in the Node class.

2.
Implement the .get_link_node() getter in the Node class.
"""
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node
    
  # Define your get_value and get_link_node methods below:
  def get_value(self):
    return self.value
  def get_link_node(self):
    return self.link_node