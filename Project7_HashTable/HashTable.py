class HashNode:
    """
    DO NOT EDIT
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

class HashTable:
    """
    Hash table class, utilizes double hashing for conflicts
    """

    def __init__(self, capacity=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None]*capacity

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        prints a HashTable
        :return str: string to print
        """
        for i in range(self.capacity):
            if self.table[i] is not None:
                key = self.table[i].key
                value = self.table[i].value
                print(key, ":", value, end=" ")
            else:
                print("None", end=" ")
        return ""

    def hash_function(self, x):
        """
        ---DO NOT EDIT---

        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.capacity

    def insert(self, key, value):
        """
        Inserts strings key and value into HashTable using quadratic probing.
        If load factor is greater then 0.75, then grow() is used
        Can't insert() an empty string
        :param key: string to insert into HashTable
        :param value: string to insert into HashTable
        :return: No return
        """
        # can't insert an empty string
        if value:
            # If load factor > 0.75, then grow()
            load = (self.capacity/4)*3
            if self.size > load:
                self.grow()

            node = HashNode(key, value)
            index = self.quadratic_probe(key)
            if index is not None:
                if self.table[index] is None:
                    self.size += 1
                    self.table[index] = node
                else:
                    self.table[index].value = value

    def quadratic_probe(self, key):
        """
        Runs the quadratic hashing procedure and returns the table index of the key
        If the key isn't in the table, next available index is returned
        Bucket = (Bucket + i*i) % Capacity
        :param key: string to hash
        :return: index of key, or nex available index
        """
        if len(key) == 0:
            return -1
        i = 0
        index = (self.hash_function(key) + pow(i, 2)) % self.capacity
        og = index
        if self.table[index] is not None:

            while self.table[index] is not None:

                if self.table[index].key == key:
                    return index

                i += 1
                if index == (self.capacity - 1):
                    index = 0
                else:
                    index = (self.hash_function(key) + pow(i, 2)) % self.capacity
                if index == og:
                    for i in range(len(self.table)):
                        if self.table[i] is None:
                            return i
                    return None

        return index

    def find(self, key):
        """
        key to search for in HashTable and returns the node of key
        If key isn't in the table then False is returned
        :param key: string to search for in HashTable
        :return: node of key, or False
        """
        if (self.size < 1) or (len(key) < 1):
            return False
        index = self.quadratic_probe(key)
        if index is None:
            return False
        if (self.table[index] is not None) and (self.table[index].key == key):
            return self.table[index]
        return False

    def lookup(self, key):
        """
        key to search for in HashTable and returns the value of the node
        If key isn't in the table then False is returned
        :param key: string to search for in HashTable
        :return: value of node, or False
        """
        node = self.find(key)
        if node is not False:
            return node.value
        return node

    def delete(self, key):
        """
        key to delete in HashTable by setting the node to None
        If key isn't in the table then False is returned
        :param key: key to delete in HashTable
        :return: no return
        """
        if self.size != 0:
            index = self.quadratic_probe(key)
            if (self.table[index] is not None) and (self.table[index].key == key):
                self.table[index] = None
                self.size -= 1

    def grow(self):
        """
        Doubles the capacity of the HashTable and rehashes all items in the HashTable
        :return: no return
        """
        load = (self.capacity / 4) * 3
        if self.size > load:
            table = HashTable(self.capacity*2)
            for i in range(len(self.table)):
                table.table[i] = self.table[i]
            self.table = table.table
            self.capacity = table.capacity
            self.rehash()

    def rehash(self):
        """
        Rehashes all items in the the HashTable
        :return: no return
        """
        table = HashTable(self.capacity)
        for i in range(len(self.table)):
            if self.table[i] is not None:
                table.insert(self.table[i].key, self.table[i].value)
        self.table = table.table


def string_difference(string1, string2):
    """
    Uses HashTable to get the difference of characters
    Returns a set of the different characters, grouped by characters
    :param string1: string to compare
    :param string2: string to compare
    :return: set of the different characters, grouped by characters
    """
    len1 = len(string1)
    len2 = len(string2)

    tb1 = HashTable()
    dif = set()
    for i in range(len1):
        val = tb1.lookup(string1[i])
        if val is False:
            val = 1
        else:
            val = int(val) + 1
        tb1.insert(string1[i], str(val))

    for i in range(len2):
        val = tb1.lookup(string2[i])
        if val is False:
            val = -1
        else:
            val = int(val) - 1
        tb1.insert(string2[i], str(val))

    for i in range(tb1.capacity):
        table = tb1.table[i]
        if (table is not None) and (int(table.value) != 0):
            dif.add(str(tb1.table[i].key)*abs(int(table.value)))
    return dif

if __name__ == '__main__':
    s1 = "missis sippi"
    s2 = "mrpaninis   "

    result = string_difference(s1, s2)
    print("result: ", result)



    s1 = "green"
    s2 = "white"

    result = string_difference(s1, s2)
    print("result: ", result)



    s1 = "blue"
    s2 = "blue"

    result = string_difference(s1, s2)
    print("result: ", result)
