# Sorting


def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    swapped_recently = True

    while swapped_recently:
        swapped_recently = False

        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                swapped_recently = True
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

    print lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    return_list = []

    while True:
        if list1:
            if list2:
                if list1[0] > list2[0]:
                    return_list.append(list2.pop(0))
                else:
                    return_list.append(list1.pop(0))
            else:
                return_list.extend(list1)
                return return_list

        else:
            return_list.extend(list2)
            return return_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """

    if len(lst) < 2:
        return lst

    index = int(len(lst) / 2)
    first_half = lst[0:index]
    second_half = lst[index:]

    sorted_first_half = merge_sort(first_half)
    sorted_second_half = merge_sort(second_half)

    sorted = merge_lists(sorted_first_half, sorted_second_half)

    return sorted

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
