class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key= None, value= None):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity): # or capacity = MIN_CAPACITY in constructor
        # Your code here
        self.capacity = MIN_CAPACITY
        self.size = 0
        self.storage = [None] * self.capacity
        

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        pass


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        pass


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
            


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for char in key:
            hash = (hash * 33) + ord(char)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """

        # take every character in the string, and convert character to number
        # Convert each character into UTF-8 numbers

        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.


        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        # self.storage[i] = value
        # self.size += 1
        
        if self.storage[i] is None: # if storage is empty
            self.storage[i] = HashTableEntry(key, value)
            self.size += 1
        else:
            cur = self.storage[i]
            while cur.key != key and cur.next != None: # while we are looping / searching for the key & the next key is not none
                cur = cur.next # move to next key
            if cur.key == key: # if we find and already existing key
                cur.value = value # update/overwrite that value
            else: # else enter the new value
                cur.next = HashTableEntry(key, value)
                self.size += 1

        # create linked list: insert at self.head (repeat)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        if self.storage[i] == None:
            return f'key is not found'
        else:
            # self.storage[i] = None
            # self.size -= 1
            cur = self.storage[i]
            while cur.key != key and cur.next != None:
                cur = cur.next
            if cur.key == key:
                cur.value = None
                self.size -= 1
            else:
                return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        i = self.hash_index(key)
        if self.storage[i] == None:
            return None
        else:
            cur = self.storage[i]
            while cur.key != key and cur.next != None:
                cur = cur.next
            if cur.key == key:
                return cur.value
            else:
                return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
