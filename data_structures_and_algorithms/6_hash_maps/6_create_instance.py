"""
Creating an Instance
Since we have the basic functionality of a hash map, let’s create a test instance of one for us to make sure everything works as expected.

Instructions
1.
Outside the HashMap class (completely unindented below the class definition) create a new hash map called hash_map. Give it an array size of 20.

2.
We want to use this hash map to store geologic information — types of rocks.

In hash_map save the value "metamorphic" for the key "gneiss".

3.
Now retrieve the value of hash_map for the key gneiss. Print it out, does your HashMap work as expected?
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
        self.array[array_index] = value

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        return self.array[array_index]

hash_map = HashMap(20)
hash_map.assign("gneiss", "metamorphic")
print(hash_map.retrieve("gneiss"))