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
        # hash = 5381
        # for x in key:
        #     hash = ((hash << 5) + hash) + ord(x)
        # return int(hash & 0xFFFFFFFF)

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # check that count is not bigger than capacity
        if self.count >= self.capacity:
            # resize the array
            self.resize()

        # First hash the key
        key = self._hash(key)

        # set key to be valid integer by passing it through _hash_mod
        key = self._hash_mod(key)

        # Shift everything that is to the right of key over by 1
        for i in range(self.count, key, -1):
            self.storage[i] = self.storage[key]

        # insert the value at the index
        self.storage[key] = value

        # increment count
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
        key = self._hash(key)

        # Covert hash to valid integer
        key = self._hash_mod(key)

        # return storage at key
        return self.storage[key]

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # set capacity to capacity times 2
        self.capacity *= 2
        # Create a new storage
        new_storage = [None] * self.capacity
        # Copy over content of storage to the new storage
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage


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
