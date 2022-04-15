"""
DOUBLY LINKED LISTS: PYTHON
Removing by Value II
Now that we’ve found the node that we want to remove from the list (or returned None if it didn’t exist), it’s time to actually remove the node. This means resetting the pointers around the node.

There are three cases here:

The node was the head of the list, in which case we can just call .remove_head()
The node was the tail of the list, in which case we can just call .remove_tail()
The node was somewhere in the middle of the list, in which case we will need to manually change the pointers for its previous and next nodes
Instructions
1.
Still in your .remove_by_value() method, check if node_to_remove is the list’s head. If so, call .remove_head().


Stuck? Get a hint
2.
Else if node_to_remove is the list’s tail, call .remove_tail().

3.
Else, we know that the node is somewhere in the middle of the list. To remove it, we will need to reset the pointers for the nodes around it. In an else block, create:

A next_node node that is equal to node_to_remove‘s next node
A prev_node node that is equal to node_to_remove‘s previous node

Stuck? Get a hint
4.
Now that we have our nodes, we can remove the pointers to and from node_to_remove and have next_node and prev_node point to each other. Still in the else block:

Set next_node‘s previous node to prev_node
Set prev_node‘s next node to next_node
5.
Finally, outside of the else block, return node_to_remove.
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

        if node_to_remove == self.head_node:
            self.remove_head()
        elif node_to_remove == self.tail_node:
            self.remove_tail()
        else:
            next_node = node_to_remove.get_next_node()
            prev_node = node_to_remove.get_prev_node()
            next_node.set_prev_node(prev_node)
            prev_node.set_next_node(next_node)

        return node_to_remove