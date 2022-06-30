"""
Creating the Hashing Function
The necessary ingredient in the hash map recipe is the hashing function. A hashing function takes a key and returns an index into the underlying array.

Hash functions need to be fast to compute so that access and retrieval can be done fast.

Instructions
1.
Create a method for HashMap called .hash(). This method should take two arguments: self and key.

Checkpoint 2 Passed
2.
Turn the key into a list of bytes by calling key.encode(). Save this into a variable called key_bytes.

.encode() is a string method that converts a string into its corresponding bytes, a list-like object with the numerical representation of each character in the string.

Checkpoint 3 Passed
3.
Turn the bytes object into a hash code by calling sum() on key_bytes. Save the result from that into a variable called hash_code.

Checkpoint 4 Passed
4.
Return hash_code.
"""

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code