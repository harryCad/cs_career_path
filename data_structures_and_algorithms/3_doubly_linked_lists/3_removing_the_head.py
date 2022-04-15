"""
DOUBLY LINKED LISTS: PYTHON
Removing the Head
Due to the added tail property, removing the head of the list in a doubly linked list is a little more complicated than doing so in a singly linked list:

Start by checking if there’s a current head to the list.
If there isn’t, the list is empty, so there’s nothing to remove and the method ends
Otherwise, update the list’s head to be the current head’s next node
If the updated head is not None (meaning the list had more than one element when we started):
Set the head’s previous node to None since there should be no node before the head of the list
If the removed head was also the tail of the list (meaning there was only one element in the list):
Call .remove_tail() to make the necessary changes to the tail of the list (we will create this method in the next exercise!)
Finally, return the removed head’s value
Instructions
1.
Define a .remove_head() method that only takes self as a parameter. Inside, create a removed_head variable and set it to the list’s head node.

Checkpoint 2 Passed
2.
Check if removed_head has no value. If so, that means there’s nothing to remove, so return None to end the method.

Checkpoint 3 Passed
3.
Outside of your if, set the list’s head to removed_head‘s next node.

If the list still has a head, set its previous node to None, since the head of the list shouldn’t have a previous node.

Checkpoint 4 Passed

Stuck? Get a hint
4.
Check if removed_head is equal to the list’s tail. If so, call the .remove_tail() method (we will create this in the next exercise).

Checkpoint 5 Passed

Stuck? Get a hint
5.
Finally, return removed_head‘s value.
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
            self.head_node.set_prev_node(None)
            return None
        self.head_node = removed_head.get_next_node()
        if self.head_node != None:
            self.head_node.set_prev_node(None)
        if self.tail_node == removed_head:
            self.remove_tail()

        return removed_head.get_value()