"""
Queues Python Dequeue
We can add items to the tail of our queue, but we remove them from the head using a method known as dequeue(), which is another way to say “remove from a queue”. Like enqueue(), we care about the size of the queue — but in the other direction, so that we prevent queue “underflow”. After all, you don’t want to remove something that isn’t there!

As with peek(), our dequeue() method should return the value of the head. Unlike, peek(), dequeue() will also remove the current head and replace it with the following node.

For dequeue, there are three scenarios that we will take into account:

The queue is empty, so we cannot remove or return any 1_nodes lest we run into queue “underflow”
The queue has one node, so when we remove it, the queue will be empty and we need to reset the queue’s head and tail to None
The queue has more than one node, and we just remove the head node and reset the head to the following node
Instructions
1.
Inside the Queue class you built, define a method dequeue().

Add an if clause to check if the queue is not empty
If so, set a new variable item_to_remove to the current head
Inside your if statement, print: “Removing “ + str(item_to_remove.get_value()) + “ from the queue!”

Stuck? Get a hint
2.
Inside the if statement, below your print statement, check if the size is 1.

If so, give the queue’s head and tail a value of None
Otherwise, set the queue’s head equal to the following node using Node‘s handy dandy get_next_node() method
3.
Outside of the inner if/else clause

reduce the queue’s size by 1
use Node‘s get_value() method to return the value of item_to_remove
4.
After the outermost if statement, create an else statement. Within it, print “This queue is totally empty!”
"""

from node import Node

class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)
            print("Adding " + str(item_to_add.get_value()) + " to the queue!")
            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("Sorry, no more room!")

    # Add your dequeue method below:
    def dequeue(self):
        if not self.is_empty():
            item_to_remove = self.head
            print(f"Removing {str(item_to_remove.get_value())} from the queue!")
            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("This queue is totally empty!")

    def peek(self):
        if self.is_empty():
            print("Nothing to see here!")
        else:
            return self.head.get_value()

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None:
            return True
        else:
            return self.max_size > self.get_size()

    def is_empty(self):
        return self.size == 0

q = Queue()
q.enqueue("some guy with a mustache")
q.dequeue()