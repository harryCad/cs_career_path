"""
Adding to the Head
In a singly linked list, we can add to the head of the list by checking to see if it already has a head. We then either set the new node as the head (if there was no head) or update the head property, and link the past head to the new head.

Since a doubly linked list has an additional tail property and is built with 1_nodes that each have two pointers, there are a few more steps:

Start by checking to see if there is a current head to the list
If there is (meaning the list is not empty), then we want to reset the pointers at the head of the list:
Set the current head’s previous node to the new head
Set the new head’s next node to the current head
Update the head property to be the new head
Finally, if there isn’t a current tail to the list (meaning the list was empty):
Update the tail property to be the new head since that node will be both the head and tail of the list
Instructions
1.
Define an .add_to_head() method that takes self and new_value as parameters.

Inside, create:

A new_head Node that takes new_value as a parameter
A current_head Node that’s set to the list’s head
Checkpoint 2 Passed

Stuck? Get a hint
2.
If there is a current head to the list:

Set current_head‘s previous node to new_head
Set new_head‘s next node to current_head
Remember to use the Node class’s .set_prev_node() and .set_next_node() methods.

Checkpoint 3 Passed

Stuck? Get a hint
3.
Outside of the if statement, set the list’s head to new_head.

Checkpoint 4 Passed

Stuck? Get a hint
4.
Lastly, if the list doesn’t have a tail, set the list’s tail to the new head.
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