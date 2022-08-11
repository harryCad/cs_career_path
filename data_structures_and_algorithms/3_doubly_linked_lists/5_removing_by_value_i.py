"""
DOUBLY LINKED LISTS: PYTHON
Removing by Value I
In addition to removing the head and the tail of the list, it would also be useful to be able to remove a specific element from anywhere in the list.

Imagine that you have a list of errands to run. You don’t always do your errands in order, so when you finish doing your laundry and want to cross it off, that could be somewhere in the middle of the list. We are going to build a .remove_by_value() method that will allow you to cross off (remove) that errand no matter where it is in the list.

In order to do this:

Iterate through the list to find the matching node
If there is no matching element in the list:
Return None
If there is a matching node, we will then check to see if it is the head or tail of the list:
If so, call the corresponding .remove_head() or .remove_tail() method
If not, that means the node was somewhere in the middle of the list. In that case:
Remove it by resetting the pointers of its previous and next 1_nodes
Finally, return the node’s value property
Instructions
1.
Define a .remove_by_value() method that takes self and value_to_remove as parameters.

Inside it, create a node_to_remove node. We don’t know what it is yet, so set it to None.

2.
Create a current_node node and set it equal to the list’s head. Then create a while loop that runs while current_node isn’t None.

Inside the loop, update current_node to be its next node. This is how we will iterate through the list as we look for the matching node.

(If you accidentally create an infinite loop and your code won’t stop running, you can reload the page to stop it.)


Stuck? Get a hint
3.
Inside the while loop, but before you updated current_node to be its next node, create an if statement that checks if current_node‘s value matches the passed in value_to_remove. If it does, that means we have found the matching node.

Inside the if:

Set node_to_remove to current_node
break to leave the while loop, since we don’t need to keep looking through the list

Stuck? Get a hint
4.
Outside your while loop, check if node_to_remove has any value. If it doesn’t, that means there was no matching node in the list, so return None to end the method.
"""

class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return self.prev_node

    def get_value(self):
        return self.value


class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_value):
        new_head = Node(new_value)
        current_head = self.head_node
        if current_head != None:
            current_head.set_prev_node(new_head)
            new_head.set_next_node(current_head)
        self.head_node = new_head
        if self.tail_node == None:
            self.tail_node = new_head

    def add_to_tail(self, new_value):
        new_tail = Node(new_value)
        current_tail = self.tail_node
        if current_tail != None:
            current_tail.set_next_node(new_tail)
            new_tail.set_prev_node(current_tail)
        self.tail_node = new_tail
        if self.head_node == None:
            self.head_node = new_tail

    def remove_head(self):
        removed_head = self.head_node
        if removed_head == None:
            return None
        self.head_node = removed_head.get_next_node()
        if self.head_node != None:
            self.head_node.set_prev_node(None)
        if removed_head == self.tail_node:
            self.remove_tail()
        return removed_head.get_value()

    def remove_tail(self):
        removed_tail = self.tail_node
        if removed_tail == None:
            return None
        self.tail_node = removed_tail.get_prev_node()
        if self.tail_node != None:
            self.tail_node.set_next_node(None)
        if removed_tail == self.head_node:
            self.remove_head()
        return removed_tail.get_value()


    def remove_by_value(self, value_to_remove):
        node_to_remove = None
        current_node = self.head_node
        while current_node != None:
            if current_node.get_value() == value_to_remove:
                node_to_remove = current_node
                break
            current_node = current_node.get_next_node()
        if node_to_remove == None:
            return None