"""
Creating the Compression Function
Hashing functions return a wide range of integers. In order to transform these values into useful indices for our array we need a compression function. A compression function uses modular arithmetic to calculate an array index for a hash map when given a hash code.

Instructions
1.
Create a .compressor() method for your hash map.

It should take two parameters: self and hash_code.

2.
Take the modulus of the hash code by the map’s array_size in order to reduce the hash code to a possible index for the array.

Return the modulus.
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