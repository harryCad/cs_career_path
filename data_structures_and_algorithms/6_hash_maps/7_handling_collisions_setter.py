"""
Handling Collisions in the Setter
Our hash and compression functions together can result in collisions. This is when two different keys resolve to the same array index. In our current implementation, all keys that resolve to the same index are treated as if they are the same key.

Our first step in implementing a collision strategy is updating our .assign() and .retrieve() methods to set the value with the key and check the key before retrieving a value.

Instructions
1.
We’re going to overwrite the functionality for .assign(). After finding the array_index, we want to do a check of the content that’s currently at self.array[array_index].

In order to avoid overwriting the wrong key, check the existing value in the array at self.array[array_index]. Save this into current_array_value.

2.
There are three possibilities for current_array_value:

It has the same key as key.
It has a different key than key.
It’s None.
If current_array_value is equal to None, instead of just saving value, save [key, value] to the array.

3.
If current_array_value already has contents, check if the saved key is different from the key we are currently processing. If the keys are the same, overwrite the array value.

If the keys are different, we’re going to implement a way to find the next array index where our key should go. We’ll get to handling different keys later.
"""

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code

    def compressor(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]
        if current_array_value == None:
            self.array[array_index] = [key, value]
        else:
            if key == current_array_value[0]:
                self.array[array_index][1] = value
            else:
                pass

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        return self.array[array_index]
