# '''
# Linked List hash table key/value pair
# '''

import hashlib


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def _rehash(self, key):
        index = self._hash_mod(key)
        return (index + 1) % self.resize()

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        # use hash mod function to get a valid index
        index = self._hash_mod(key)
        # Check if the storage at that index is occupied
        if self.storage[index]:
            # If index position is occupied and the key is not the same as the key of the object to be added
            if self.storage[index] and self.storage[index].key != key:
                # chain a new link list
                node = self.storage[index]
                node.next = LinkedPair(key, value)
            # otherwise
            else:
                self.storage[index].value = value
        # If storage at that index is empty, set the 
        else:
            self.storage[index] = LinkedPair(key, value)
        # Increment the count of the storage
        self.count += 1

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # First hash key
        key = self._hash(key)

        # Covert hash to valid integer
        key = self._hash_mod(key)

        # Check if key is found
        if not self.storage[key]:
            print("Key not found")

        # store the value of key
        item = self.storage[key]

        # set the current count - 1 value to None
        self.storage[key] = None

        # Decrement count
        self.count -= 1
        return item

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # First hash key
        index = self._hash_mod(key)
        if self.storage[index]:
            return self.storage[index].retrieve(key)
        else:
            print(f"Hash[{key}] is undefined")
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        old_storage = self.storage
        self.storage = [None] * self.capacity

        self.storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
