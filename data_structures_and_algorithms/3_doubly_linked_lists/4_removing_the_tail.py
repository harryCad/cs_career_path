"""
DOUBLY LINKED LISTS: PYTHON
Removing the Tail
The doubly linked list’s tail property allows us to remove the tail just as easily as we could remove the head. In fact, like with the .add_to_head() and .add_to_tail() methods, the .remove_tail() method will closely mirror the .remove_head() method:

Start by checking if there’s a current tail to the list.
If there isn’t, The list is empty, so there’s nothing to remove, and the method ends
Otherwise, update the list’s tail to be the current tail’s previous node
If the updated tail is not None (meaning the list had more than one element when we started):
Set the tail’s next node to None since there should be no node after the tail of the list
If the removed tail was also the head of the list (meaning there was only one element in the list):
Call .remove_head() to make the necessary changes to the head of the list
Finally, return the old tail’s data
Instructions
1.
Define a .remove_tail() method that only has self as a parameter. Inside, create a removed_tail variable and set it to the list’s tail.

Checkpoint 2 Passed
2.
Check if removed_tail has no value. If so, that means the list is empty and there’s nothing to remove, so return None to end the method.

Checkpoint 3 Passed
3.
Outside of your if, set the list’s tail to removed_tail‘s previous node.

If the list still has a tail (meaning that the list isn’t now empty), set the tail’s next node to None, since the tail of the list shouldn’t have a next node.

Checkpoint 4 Passed

Stuck? Get a hint
4.
Check if removed_tail is equal to the list’s head. If so, call the .remove_head() method.

Checkpoint 5 Passed
5.
Finally, return removed_tail‘s value.
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