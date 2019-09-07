"""
PROJECT 3 - Hybrid Sorting
Name: Ben Traines
PID: A51468549
"""


def merge_sort(unsorted, threshold, reverse):
    """
    Recursive sort that returns a sorted list by splitting the list
    in half until a threshold then insertion_sort is used.
    :param unsorted: list to sort
    :param threshold: When to switch to insertion_sort
    :param reverse: if False sort in increasing order
    """
    unsorted_length = len(unsorted)
    if (threshold == 0) and (unsorted_length <= 1):
        return unsorted
    elif unsorted_length > threshold:
        unsorted_midpoint = unsorted_length // 2

        unsorted_first_list = unsorted[:unsorted_midpoint]
        unsorted_second_list = unsorted[unsorted_midpoint:]

        unsorted_first_list = merge_sort(unsorted_first_list, threshold, reverse)
        unsorted_second_list = merge_sort(unsorted_second_list, threshold, reverse)
        unsorted = merge(unsorted_first_list, unsorted_second_list, reverse)
    else:
        insertion_sort(unsorted, reverse)

    return unsorted


def merge(first, second, reverse):
    """
    merges two lists together and returns a single sorted list
    :param first: list one
    :param second: list two
    :param reverse: if False sort in increasing order
    :return: A single sorted list
    """

    merged_list = [0] * (len(first) + len(second))
    merge_pos = 0
    first_elem_pos = 0
    first_length = len(first) - 1
    second_elem_pos = 0
    second_length = len(second) - 1

    while (first_elem_pos <= first_length) and (second_elem_pos <= second_length):
        if reverse:
            if first[first_elem_pos] >= second[second_elem_pos]:
                merged_list[merge_pos] = first[first_elem_pos]
                first_elem_pos += 1
            else:
                merged_list[merge_pos] = second[second_elem_pos]
                second_elem_pos += 1
            merge_pos += 1
        else:
            if first[first_elem_pos] <= second[second_elem_pos]:
                merged_list[merge_pos] = first[first_elem_pos]
                first_elem_pos += 1
            else:
                merged_list[merge_pos] = second[second_elem_pos]
                second_elem_pos += 1
            merge_pos += 1

    while first_elem_pos <= first_length:
        merged_list[merge_pos] = first[first_elem_pos]
        first_elem_pos += 1
        merge_pos += 1

    while second_elem_pos <= second_length:
        merged_list[merge_pos] = second[second_elem_pos]
        second_elem_pos += 1
        merge_pos += 1
    return merged_list


def insertion_sort(unsorted, reverse):
    """
    Sorts a llist using insertion_sort and returns the list
    :param unsorted: list to sort
    :param reverse: if False sort in increasing order
    """

    for i in range(1, len(unsorted)):
        j = i

        if reverse:
            while j > 0 and unsorted[j] > unsorted[j - 1]:
                temp = unsorted[j]
                unsorted[j] = unsorted[j - 1]
                unsorted[j - 1] = temp
                j -= 1
        else:
            while j > 0 and unsorted[j] < unsorted[j - 1]:
                temp = unsorted[j]
                unsorted[j] = unsorted[j - 1]
                unsorted[j - 1] = temp
                j -= 1