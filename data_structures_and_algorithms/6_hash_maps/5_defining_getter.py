"""
Defining the Getter
There is a natural expectation after placing an item into a bag that we will later be able to remove the item from that bag. Otherwise we have created a hole. Let’s implement retrieval for our hash map.

Instructions
1.
Define a .retrieve()method for HashMap. It should take two parameters: self and key.

2.
.retrieve() should calculate the array index in the same way our .assign() does and then retrieve the value at that index.

Return that value.
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