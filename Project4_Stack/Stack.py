"""
# Project 4
# Name: Ben Traines
# PID: A51468549
"""

class Stack:
    """
    Stack class
    """
    def __init__(self, capacity=2):
        """
        DO NOT MODIFY
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack. Default size 2.
        """
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0

    def __str__(self):
        """
        DO NOT MODIFY
        Prints the values in the stack from bottom to top. Then, prints capacity.
        :return: string
        """
        if self.size == 0:
            return "Empty Stack"

        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def __eq__(self, stack2):
        """
        DO NOT MODIFY
        Checks if two stacks are equivalent to each other. Checks equivalency of data and capacity
        :return: True if equal, False if not
        """
        if self.capacity != stack2.capacity:
            return False

        count = 0
        for item in self.data:
            if item != stack2.data[count]:
                return False
            count += 1

        return True

    def stack_size(self):
        """
        Returns the current number of items in the stack
        :param self: the stack
        :return: # of items in stack
        """
        return self.size

    def is_empty(self):
        """
        Checks if the given stack is empty
        :param self: the stack
        :return: True if the stack is empty, otherwise False
        """
        if self.size == 0:
            return True
        else:
            return False

    def top(self):
        """
        Returns the top item from the stack or None if stack is empty. Doesn't remove item from stack
        :param self: the stack
        :return: top item of the stack
        """
        return self.data[self.size - 1]

    def push(self, val):
        """
        Adds val to the top of the stack
        :param self: the stack
        :param val: the val to add to the stack
        """
        if self.size == self.capacity:
            self.grow()
        self.size += 1
        self.data[self.size - 1] = int(val)

    def pop(self):
        """
        Removes the top item from the stack by setting it to None and returns the new top item or None
        :param self: the stack
        :return: top item of the stack or None
        """
        top = self.data[0]
        if self.size > 0:
            top = self.data[self.size-1]
        self.data[self.size - 1] = None
        if self.size > 0:
            self.size -= 1
        if (self.size <= (self.capacity / 2)) and (self.capacity > 2):
            self.shrink()
        return top

    def grow(self):
        """
        Doubles the capacity of the queue immediately when capacity is reached to make room for new elements
        Moves the head to the front of the newly allocated list
        """
        self.data.extend(([None] * self.capacity))
        self.capacity = self.capacity * 2

    def shrink(self):
        """
        Halves the capacity of the queue if the size is 1/4 of the capacity
        Capacity should never go below 4
        Moves the head to the front of the newly allocated list
        """

        old_cap = self.capacity
        self.capacity = (self.capacity // 2)
        del self.data[self.capacity:old_cap]


def reverse(stack):
    """
    Reverse the order of the given stack and returns the stack
    :param stack: the stack
    :return: reversed stack
    """
    rev_stack = Stack(stack.capacity)
    stack_size = stack.size
    for i in range(stack_size):
        top = stack.pop()
        rev_stack.push(top)
        i += i
    return rev_stack


def replace(stack, old, new):
    """
    Replaces every int old in stack with new, and returns the updated stack
    :param stack: the stack
    :param old: old int to replace
    :param new: int to replace old with
    :return: updated stack
    """
    for i in range(stack.size):
        if stack.data[i] == old:
            stack.data[i] = new
        i += i
    return stack