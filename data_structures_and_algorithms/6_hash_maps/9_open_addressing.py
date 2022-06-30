"""
Open Addressing
Now we’re going to implement an open addressing system so our hash map can resolve collisions. In open addressing systems, we check the array at the address given by our hashing function. One of three things can happen:

The address points to an empty cell.
The cell holds a value for the key we are getting/setting
The cell holds a value for a different key.
In the first case, this means that the hash map does not have a value for the key and no collision resolution needs to happen. Notice that this does not work if we want to be able to delete keys in our hash map. There are strategies for deleting pairs from a hash map (see Lazy Deletion) but we will not be investigating these.

In the second case, we’ve found the value for our key-value pair!

In the third case, we need to use our collision addressing strategy to find if our key is somewhere else (it may or may not be) so we should recalculate the index of our array.

Instructions
1.
Give HashMap.hash() another parameter: count_collisions. This will be the number of times the .hash() has hit a collision.

Have count_collisions default to 0.


Stuck? Get a hint
2.
Instead of returning hash_code from .hash(), return hash_code + count_collisions.
"""

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions = 0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # current_array_value currently holds different key
        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        # possible_return_value holds different key
        return
