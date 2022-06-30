"""
Creating the Hash Map Class
Hash maps are efficient key-value stores. They are capable of assigning and retrieving data in the fastest way possible for a data structure. This is because the underlying data structure that they use is an array. A value is stored at an array index determined by plugging the key into a hash function.

In Python we don’t have an array data structure that uses a contiguous block of memory. We are going to simulate an array by creating a list and keeping track of the size of the list with an additional integer variable. This will allow us to design something that resembles a hash map. This is somewhat elaborate for the actual storage of a key-value pair, but it helps to remember that the purpose of this lesson is to gain a deeper understanding of the structure as it is constructed. For real-world use cases in which a key-value store is needed, Python offers a built-in hash table implementation with dictionaries.

Instructions
1.
Create a class called HashMap.


Stuck? Get a hint
2.
Give HashMap a constructor which takes both self and array_size as parameters. array_size should be assigned to an instance variable of the same name (.array_size), and represents the size of the array.


Stuck? Get a hint
3.
Create an instance variable called .array, which is a list of size array_size. Make each element of .array equal to None.
"""

class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None] * self.array_size