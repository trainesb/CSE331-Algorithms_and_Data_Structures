"""
# Project 5
# Name: Ben Traines
# PID: A51468549
"""


class CircularQueue():
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0

    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    # -----------MODIFY BELOW--------------

    def __str__(self):

        if self.size == 0:
            return "Empty Stack"

        output = []
        i = 0
        while i != (self.capacity):
            output.append(str(self.data[i]))
            i += 1
        return "{} Capacity: {}".format(output, str(self.capacity))

    def is_empty(self):
        """
        Returns if empty or not (bool)
        :return: true if empty, false otherwise
        """
        if self.size == 0:
            return True
        return False

    def __len__(self):
        """
        Returns the size of the queue
        :return: size of queue
        """
        return self.size

    def first_value(self):
        """
        Returns the front of the queue
        :return: front of queue
        """
        return self.data[self.head]

    def enqueue(self, val):
        """
        Adds val to the back of the queue
        :param val: val to add to queue
        :return: None
        """
        if (self.size == self.capacity) or (self.tail+1) == self.capacity:
            self.grow()
        self.data[self.tail] = val
        self.size += 1
        self.tail += 1
        return None

    def dequeue(self):
        """
        Remove first_val from queue if not empty, and return the removed val
        :return: removed val
        """
        if not self.is_empty():

            tmp_size = self.size - 1
            self.size = tmp_size
            old_first_val = self.data[self.head]
            self.data[self.head] = None
            self.head += 1
            self.shrink()
            return old_first_val

    def grow(self):
        """
        Doubles the capacity of the queue immediately when capacity is reached
        :return: No Return
        """
        if self.capacity < 4:
            self.capacity = 4
        if (self.size + 1) == self.capacity:
            queue = CircularQueue(self.capacity * 2)
        else:
            queue = CircularQueue(self.capacity)
        i = self.head
        pos = 0
        while i < self.tail:
            queue.data[pos] = self.data[i]
            queue.size += 1
            queue.tail = queue.size
            self.data[i] = None
            i += 1
            pos += 1
        self.head = queue.head
        self.tail = queue.size
        self.data = queue.data
        self.capacity = queue.capacity

    def shrink(self):
        """
        Halves the capacity of the queue if the size is 1/4 of the capacity
        Capacity should never go below 4
        Moves the head to the front of the newly allocated list
        :return: No Return
        """
        new_capacity = self.capacity // 2
        if (self.size <= (self.capacity // 4)) and (new_capacity > 3):
            i = self.head
            pos = 0
            queue = CircularQueue(new_capacity)

            while i <= self.tail and self.data[i] is not None:
                queue.data[pos] = self.data[i]
                queue.size += 1
                queue.tail = queue.size
                self.data[i] = None
                i += 1
                pos += 1
            self.head = queue.head
            self.tail = queue.tail
            self.data = queue.data
            self.capacity = queue.capacity
            self.shrink()


if __name__ == '__main__':

    qu = CircularQueue()
    qu.enqueue(1)
    qu.enqueue(2)
    qu.enqueue(3)
    qu.enqueue(4)
    qu.enqueue(5)
    qu.enqueue(6)
    qu.enqueue(7)
    qu.enqueue(8)
    print('Queue: ', qu, ' Size: ', qu.size)
    print('Head[', qu.head, ']: ', qu.data[qu.head])
    print('Tail[', qu.tail, ']: ', qu.data[qu.tail])

    print('\nRemove:')
    for i in range(4):
        qu.dequeue()
        print('\tQueue: ', qu, ' Size: ', qu.size)
        print('\tHead[', qu.head, ']: ', qu.data[qu.head])
        print('\tTail[', qu.tail, ']: ', qu.data[qu.tail])
    print('Queue: ', qu, ' Size: ', qu.size)
    print('Head[', qu.head, ']: ', qu.data[qu.head])
    print('Tail[', qu.tail, ']: ', qu.data[qu.tail])


    print('\nAdd:')
    for i in range(3):
        qu.enqueue(i)
        print('\tQueue: ', qu, ' Size: ', qu.size)
        print('\tHead[', qu.head, ']: ', qu.data[qu.head])
        print('\tTail[', qu.tail, ']: ', qu.data[qu.tail])

    print('Queue: ', qu, ' Size: ', qu.size)
    print('Head[', qu.head, ']: ', qu.data[qu.head])
    print('Tail[', qu.tail, ']: ', qu.data[qu.tail])