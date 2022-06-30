"""
Defining the Setter
A data structure that is unable to contain data is a sad sight indeed. We need to put together all the other steps we’ve taken: plug the key into the hash function, plug the hash code into the compression function, use the array index to find the place in the array, and finally set the value of the array to the value we want.

Instructions
1.
Create a .assign() method for the hash map. It should take three parameters: self, key, and value.

Checkpoint 2 Passed
2.
Save the value (just the value for now) to the map’s array at the index determined by plugging the key into the .hash() method and plugging the hash code into the .compressor() method.
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
        index = self.compressor(self.hash(key))
        self.array[index] = value