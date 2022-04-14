"""
Queues Python Size
Bounded queues require limits on the number of nodes that can be contained, while other queues don’t. To account for this, we will need to make some modifications to our Queue class so that we can keep track of and limit size where needed.

We’ll be adding two new properties to help us out here:

A size property to keep track of the queue’s current size
A max_size property that bounded queues can utilize to limit the total node count
In addition, we will add three new methods:

get_size() will return the value of the size property
has_space() will return True if the queue has space for another node
is_empty() will return true if the size is 0
Instructions
1.
Add a new parameter max_size to your __init__() method that has a default value of None. Inside the method:

create a max_size instance variable assigned to max_size
create another instance variable size and set it equal to 0
2.
Inside Queue define a new method get_size() that returns the size instance property.

3.
Below get_size(), define another method has_space(). Inside the method, check if a self.max_size has been set.

If there’s no max_size set, then we will always have space in the queue, so we can return True
If so, return True if the max_size is greater than self.get_size()

Stuck? Get a hint
4.
Define another method is_empty for Queue. The method should return True if the queue is empty (if the size of the queue is 0).

5.
Now we’ll make sure we aren’t attempting to peek() on an empty queue. After all, a deli server can’t get an order from a line with no customers!

At the top of your peek() method body, use get_size() to see if the queue is empty.

if so, the method should just print “Nothing to see here!”
if not, peek() will perform the same as it did before
"""

from node import Node

class Queue:
    # Add max_size and size properties within __init__():
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def peek(self):
        if self.size > 0:
            return self.head.get_value()
        else:
            print("Nothing to see here!")


    # Define get_size() and has_space() below:
    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size == None or self.max_size > self.get_size():
            return True
        return False

    def is_empty(self):
        if self.size == 0:
            return True
        return False