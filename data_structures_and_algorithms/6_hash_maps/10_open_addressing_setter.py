"""
Open Addressing in the Setter
Now lets use our open addressing scheme in the setter for our HashMap.

Instructions
1.
Now that we have a hash function that uses the number of collisions to determine the hash code, we can update where we set a key in the event of a collision.

When we notice that the key we’re trying to set is different from the key at our hash code’s address, create a new variable called number_collisions, set that equal to 1.

2.
After defining number_collisions, create a new while loop that checks if current_array_value[0] != key.

3.
In the while loop, you want to replicate our setting logic while incrementing the number of collisions.

Call .hash() with both the key and number_collisions. Save that result into new_hash_code.

4.
Plug new_hash_code into .compressor(). Save that result into new_array_index.

5.
Check self.array at new_array_index and save the result as current_array_value. Check against the three possibilities:

If it’s None, save the [key, value] at self.array[new_array_index] and then return.
If it has a value, but the same key as key, overwrite the array at that address with [key, value] and then return.
If it has a value, but a different key, increment number_collisions.
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

        # current_array_value currently holds different key
        number_collisions = 1
        while current_array_value[0] != key:
            new_hash_code = self.hash(key,number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]
            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return
            elif current_array_value[0] == key and current_array_value[1] is not None:
                self.array[new_array_index] = [key,value]
            elif current_array_value[0] != key and current_array_value[1] is not None:
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
        return
