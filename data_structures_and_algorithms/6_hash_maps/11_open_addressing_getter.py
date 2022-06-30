"""
Open Addressing in the Getter
With everything in our setter taken care of, we want to make sure that when we retrieve our value we’re retrieving the correct value.

Instructions
1.
In .retrieve() if possible_return_value has a different key than the one we’re looking for, we should continue searching.

Define a new variable called retrieval_collisions and set it equal to 1.


Stuck? Get a hint
2.
Insert a new while loop that checks if

possible_return_value[0] != key
In the while loop, we want to replicate our retrieval logic while increasing the count of retrieval_collisions so that we continue to look at other locations within our array.

Call .hash() with both the key and retrieval_collisions. Save that result into new_hash_code.

3.
Plug new_hash_code into .compressor(). Save that result into retrieving_array_index.

4.
Check self.array at retrieving_array_index and save the result as possible_return_value. Check against the three possibilities:

If it’s None, return None
If it has a value, but a different key, increment retrieval_collisions.
If it’s key matches our key return possible_return_value[1].
"""

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
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

        # Collision!

        number_collisions = 1

        while(current_array_value[0] != key):
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1

        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        # possible_return_value holds different key
        retrieval_collisions = 1
        while possible_return_value[0] != key:
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]
            if possible_return_value is None:
                return None
            elif possible_return_value[1] is not None and possible_return_value[0] != key:
                retrieval_collisions += 1
            elif possible_return_value[0] == key:
                return possible_return_value[1]

        return
