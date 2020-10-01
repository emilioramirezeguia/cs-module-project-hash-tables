class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"HashTableEntry({self.key},{self.value})"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.buckets = [None] * capacity
        self.items = 0

    # def __repr__(self):

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.items / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # FNV_offset_basis (in hex, 0xcbf29ce484222325)
        FNV_offset_basis = 14695981039346656037
        # FNV_prime (in hex, 0x100000001b3)
        FNV_prime = 1099511628211
        bytes = key.encode()

        hash = FNV_offset_basis
        for byte in bytes:
            hash = hash * FNV_prime
            hash = hash ^ byte

        return hash

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        bytes = key.encode()

        for byte in bytes:
            hash = ((hash * 33) ^ byte) % 0x100000000

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        index = self.hash_index(key)
        new_node = HashTableEntry(key, value)
        current_node = self.buckets[index]

        # if linked list is empty
        if current_node is None:
            self.buckets[index] = new_node
            self.items += 1
            return

        # if linked list has something in there and we
        # get a key that matches
        while current_node is not None:
            if current_node.key == key:
                current_node.value = value
            current_node = current_node.next

        # else if no key matched
        new_node.next = self.buckets[index]
        self.buckets[index] = new_node
        self.items += 1

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        current_node = self.buckets[index]

        # if linked list is empty
        if current_node is None:
            return None

        # if node is in the head position
        if current_node.key == key:
            self.buckets[index] = current_node.next
            self.items -= 1
            return

        previous_node = current_node
        current_node = current_node.next
        # if node in the middle or the end position
        while current_node is not None:
            if current_node.key == key:
                # previous_node.next should point to current_node.next
                previous_node.next = current_node.next
                self.items -= 1
                return
            current_node = current_node.next
        # else if no key matched
        print("No matching key was found.")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        current_node = self.buckets[index]

        # if linked list is empty
        if current_node is None:
            return None
        # if linked list has something in there and we
        # get a key that matches
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next

        # else if no key matched
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.

        # save old list as a variable
        # update the current capacity to the new capacity
        # create a new list full of Nones equal to the updated capacity
        # reset items count
        # iterate through old buckets, traverse through each linked list, call put() on each node and update item count
        """
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [None] * self.capacity
        self.items = 0
        for node in old_buckets:
            while node is not None:
                self.put(node.key, node.value)
                self.items += 1
                node = node.next


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
# test_table = HashTable(8)
# test_table.put("key-0", "val-0")
# test_table.put("key-1", "val-1")
# test_table.put("key-2", "val-2")
# test_table.put("key-3", "val-3")
# test_table.put("key-4", "val-4")
# test_table.put("key-5", "val-5")
# test_table.put("key-6", "val-6")
# test_table.put("key-7", "val-7")
# test_table.put("key-8", "val-8")
# test_table.put("key-9", "val-9")
# print("Should be val-0:", test_table.get("key-0"))
# print("Should be val-1:", test_table.get("key-1"))
# print("Should be val-2", test_table.get("key-2"))
# print("Should be val-3", test_table.get("key-3"))
# print("Should be val-4", test_table.get("key-4"))
# print("Should be val-5", test_table.get("key-5"))
# print("Should be val-6", test_table.get("key-6"))
# print("Should be val-7", test_table.get("key-7"))
# print("Should be val-8:", test_table.get("key-8"))
# print("Should be val-9:", test_table.get("key-9"))
# test_table.delete("key-1")
# test_table.delete("key-3")
# test_table.delete("key-5")
# test_table.delete("key-7")
# test_table.delete("key-9")
# print("Should be val-0:", test_table.get("key-0"))
# print("Should be None:", test_table.get("key-1"))
# print("Should be val-2", test_table.get("key-2"))
# print("Should be None", test_table.get("key-3"))
# print("Should be val-4", test_table.get("key-4"))
# print("Should be None", test_table.get("key-5"))
# print("Should be val-6", test_table.get("key-6"))
# print("Should be None", test_table.get("key-7"))
# print("Should be val-8:", test_table.get("key-8"))
# print("Should be None:", test_table.get("key-9"))
