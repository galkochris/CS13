#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    #Best case: O(1); first item in array
    #Worst case: O(n): item not in the array
    #Average case: 0(n/2): average case would be half the length of the array
    # DONE: implement linear search recursively here
    if index > (len(array) - 1):
        return
    
    if item == array[index]:
        return index


    return linear_search_recursive(array, item, (index + 1))   
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    #Best Case: O(1); Only takes the first step (item in middle of array)
    #Worse Case: O(log(n)); Item not in list, iterates over whole array
    #Average Case: ~O(log(n)/2); Generally takes log(n) but some items are middle indexes
    # TODO: implement binary search iteratively here
    array.sort()
    for index, value in enumerate(array):
        if item > value:
            (len(array) - 1) / 2
    
    index = 0
    while index < (len(array) - 1):
        index = (len(array) - 1)//2
        if array[index] == item:
            return index
        if array[index] > item:
            go left
        else:
            go right
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    #Generally the same O notation as iterative, possibly slower the larger you get as stack gets larger
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
