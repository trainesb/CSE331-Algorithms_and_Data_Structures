########################################
# PROJECT: Binary Min Heap and Sort
# Author: Ben Traines
########################################

class BinaryMinHeap:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self):
        """
        Creates an empty hash table with a fixed capacity
        """
        self.table = []


    def __eq__(self, other):
        """
        Equality comparison for heaps
        :param other: Heap being compared to
        :return: True if equal, False if not equal
        """
        if len(self.table) != len(other.table):
            return False
        for i in range(len(self.table)):
            if self.table[i] != other.table[i]:
                return False

        return True

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def __str__(self):
        """
        Formats the list to print
        :return: string to print
        """
        str_list = ''
        for i in range(len(self.table)):
            str_list += str(self.table[i]) + " "
        return str_list

    def get_size(self):
        """
        Returns # of nodes in the Heap
        :return: Returns # of nodes in the Heap
        """
        return len(self.table)

    def parent(self, position):
        """
        Finds the parent node of position
        :param position: node to find the parent of
        :return: Index of parent node
        """
        return (position - 1) // 2

    def left_child(self, position):
        """
        Finds the left child at position
        :param position: node to find left child of
        :return: Index of the left node
        """
        return 2*position + 1

    def right_child(self, position):
        """
        Finds the right child at position
        :param position: node to find right child of
        :return: Index of the right node
        """
        return 2*position + 2

    def has_left(self, position):
        """
        Checks if node at position has a left child
        :param position: node to check for left child
        :return: True if node at position has a left child, else False
        """
        return self.left_child(position) < self.get_size()

    def has_right(self, position):
        """
        Checks if node at position has a right child
        :param position: node to check for right child
        :return: True if node at position has a right child, else False
        """
        return self.right_child(position) < self.get_size()

    def find(self, value):
        """
        Finds the index of the node with value
        :param value: value of the node to find
        :return: Index of the node with value, else None
        """
        for i in range(self.get_size()):
            if value == self.table[i]:
                return i
        return None

    def heap_push(self, value):
        """
        Adds a node with value to the heap, if its a duplicate nothing happens
        :param value: value to add
        :return: nothing
        """
        if self.find(value) is None:

            # Add value to end
            self.table.append(value)

            # Percolate up to correct position
            self.percolate_up(self.get_size()-1)

    def heap_pop(self, value):
        """
        Removes a node with value from the heap
        :param value: value of the node to remove from the heap
        :return: value of the node removed from the heap, else None
        """
        if self.get_size() == 0:
            return None
        val_rmv = self.find(value)
        if val_rmv is not None:
            self.swap(val_rmv, self.get_size()-1)
            val_rmvd = self.table.pop()
            self.percolate_down(val_rmv)
            return val_rmvd
        return None

    def pop_min(self):
        """
        Removes the node with the smallest value from the heap
        :return: Value of the removed node, else None
        """
        if self.get_size() == 0:
            return None
        # Swap the min to the end
        self.swap(0, self.get_size()-1)

        # Remove the min
        rmvd = self.table.pop()

        # Put the new root in its correct position
        self.percolate_down(0)

        return rmvd

    def swap(self, p1, p2):
        """
        Swap the position of the nodes at p1 and p2
        :param p1: node at p1
        :param p2: node at p2
        :return: nothing
        """
        self.table[p1], self.table[p2] = self.table[p2], self.table[p1]

    def percolate_up(self, position):
        """
        Moves the node at position up the tree to it's proper spot
        :param position: Position of the node to move
        :return: nothing
        """
        parent = self.parent(position)

        if position > 0 and self.table[position] < self.table[parent]:
            self.swap(position, parent)
            self.percolate_up(parent)

    def percolate_down(self, position):
        """
        Moves a node at position down the tree the it's proper spot
        :param position: Position of the node to move
        :return: nothing
        """

        if self.has_left(position):
            left = self.left_child(position)
            sm_child = left
            if self.has_right(position):
                right = self.right_child(position)
                if self.table[right] < self.table[left]:
                    sm_child = right
            if self.table[sm_child] < self.table[position]:
                self.swap(position, sm_child)
                self.percolate_down(sm_child)


def heap_sort(unsorted):
    """
    Performs heap sort on an unsorted list
    :param unsorted: an unsorted list
    :return: A sorted list
    """
    heap = BinaryMinHeap()
    sorted = []
    for i in range(len(unsorted)):
        heap.heap_push(unsorted[i])
    for i in range(len(heap.table)):
        sorted.append(heap.pop_min())
    return sorted