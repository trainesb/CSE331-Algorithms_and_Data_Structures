"""
PROJECT 2 - Recursion
Name: Ben Traines
PID: A51468549
"""

from Project2.LinkedNode import LinkedNode


def insert(value, node=None):
    """
    Inserts value into linked list, keeping ascending order
    :param value: value to insert
    :param node: head node of linked list to be inserted into
    :return: head node of updated list
    """
    head = node
    prev = node
    cnt = 0
    while node is not None:
        cnt += 1
        if value <= node.value:
            new_node = LinkedNode(value, node)
            if head.value >= new_node.value:
                return new_node
            prev.next_node = new_node
            if head != node:
                return head
            else:
                return new_node
        prev = node
        node = node.next_node
    if cnt:
        prev.next_node = LinkedNode(value, None)
    else:
        head = LinkedNode(value, None)
    return head


def string(node):
    """
    Creates a string representation of the linked list
    :param node: head node of linked list and starting point
    :return: string representation of the list
    """
    string_list = ''
    next_node = node
    while next_node is not None:
        string_list += str(next_node.value)
        string_list += ', '
        next_node = next_node.next_node
    string_list = string_list[:-2]
    return string_list

def reversed_string(node):
    """
    Creates a string representation of the linked list in reverse order
    :param node: head node of linked list and end point
    :return: string representation of the list
    """
    rev_list = string(node)
    rev_list = rev_list[::-1]
    rev_list = rev_list.replace(" ,", ", ")
    return rev_list


def remove(value, node):
    """
    Remove first node in the list that == value
    :param value: the value to remove in the list
    :param node: head node of linked list
    :return: head node of updated linked list
    """
    head = node
    prev = node
    node_num = 0
    while node is not None:
        node_num += 1
        if value == node.value:
            if length(head) == 1:
                return None
            elif node_num == 1:
                node = node.next_node
                return node
            prev.next_node = node.next_node
            node = node.next_node
            if head != node:
                return head
            else:
                return node
        prev = node
        node = node.next_node
    return head



def remove_all(value, node):
    """
    Remove all nodes in the list that == value
    :param value: the value to remove in the list
    :param node: head node of linked list
    :return: head node of updated linked list
    """
    head = node
    while search(value, head):
        head = remove(value, head)
    return head


def search(value, node):
    """
    Searches list for value
    :param value: the value to search for in the list
    :param node: head node of linked list
    :return: true if in the list, else false
    """
    while node is not None:
        if value == node.value:
            return True
        node = node.next_node
    return False


def length(node):
    """
    finds the length of linked list
    :param node: head node of linked list
    :return: length of linked list
    """
    lngth = 0
    while node is not None:
        lngth += 1
        node = node.next_node
    return lngth


def sum_all(node):
    """
    finds the sum of all elements of linked list
    :param node: head node of linked list
    :return: sum
    """
    sum_list = 0
    while node is not None:
        sum_list += node.value
        node = node.next_node
    return sum_list


def count(value, node):
    """
    Counts how many times value is in linked list
    :param value: value to count for
    :param node: head node of linked list
    :return: count of value in linked list
    """
    cnt = 0
    while node is not None:
        if node.value == value:
            cnt += 1
        node = node.next_node
    return cnt
