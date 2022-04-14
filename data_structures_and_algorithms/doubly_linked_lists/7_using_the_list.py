"""
DOUBLY LINKED LISTS: PYTHON
Using the List
You finished your DoublyLinkedList class! Now we’re going to use that class to model a subway line. A doubly linked list is a great data structure to use to model a subway, as both have a first and last element, and are comprised of nodes (or stops) with links to the elements before and after them.

We will add to and remove stops from our subway line, and print it out to see what we’ve done. The .stringify_list() method is the same as the one from the LinkedList class and has been provided for you.

Instructions
1.
We’re going to model a (fictional) subway line that will travel from Central Park to the Brooklyn Bridge.

At the bottom of script.py, outside the DoublyLinkedList class, create a new DoublyLinkedList named subway.


Stuck? Get a hint
2.
The subway starts at Central Park and winds its way downtown. In the following order:

Add "Times Square" to the head of the list
Add "Grand Central" to the head of the list
Add "Central Park" to the head of the list
Then print the list.


Stuck? Get a hint
3.
The subway continues from Times Square down to the Brooklyn Bridge. In the following order:

Add "Penn Station" to the tail of the list
Add "Wall Street" to the tail of the list
Add "Brooklyn Bridge" to the tail of the list
Then print the list again.


Stuck? Get a hint
4.
Oh no! There’s construction happening on the subway line: the Central Park and Brooklyn Bridge stops will temporarily be closed.

Remove them from your list without iterating through the entire list.

Then print the list again.


Stuck? Get a hint
5.
It turns out that the Times Square station is under construction as well. Remove it from the list, and then print the list for the last time.
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

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node
        while current_node:
            if current_node.get_value() != None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

# Create your subway line here:
subway = DoublyLinkedList()
subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")

subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")

subway.remove_head()
subway.remove_tail()
subway.remove_by_value("Times Square")

print(subway.stringify_list())