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
        # Get a valid index
        index = self._hash_mod(key)
        # Check if the key is in the storage
        if self.storage[index]:
            # Set it to none
            self.storage[index] = None
            # Decrement count
            self.count -= 1
        else:
            print(f"{key} not found")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index]:
            if self.storage[index].key != key:
                return self.storage[index].next.value
            else:
                return self.storage[index].value
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        new_storage = [None] * self.capacity * 2

        for i in range(self.capacity):
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
