#!python

from binarytree import BinarySearchTree

class TreeSet:
    def __init__(self, elements=None):
    ''' __init__(elements=None) - initialize a new empty set structure, and add each element if a sequence is given '''
        self.tree = BinarySearchTree()
        if elements is not None:
            for element in elements:
                self.add(element)

    def size(self):
        '''size - property that tracks the number of elements in constant time'''
        self.tree.size()
    def contains(self, element):
        '''contains(element) - return a boolean indicating whether element is in this set'''
        self.tree.contains(element)
    def add(self, element):
        '''add(element) - add element to this set, if not present already'''
        self.tree.insert(element)
    def remove(self, element):
        '''remove(element) - remove element from this set, if present, or else raise KeyError'''
        if self.tree.contains(element):
            ### can't None, add method to hide value from contains instead
            self.tree.node.data = None
    def union(self, other_set):
        '''union(other_set) - return a new set that is the union of this set and other_set'''
        new_set = TreeSet()
        for element in self.tree.items_in_order():
            if other_set.contains(element):
                new_set.add(element)
        
        return TreeSet.add(for i, j in zip(self.tree, other_set): i, j if i != j)

    def intersection(self, other_set):
        ''' intersection(other_set) - return a new set that is the intersection of this set and other_set '''
        ### REFACTOR THIS ###
        new_set = TreeSet()
        for element in self.tree.items_in_order():
            if other_set.contains(element):
                new_set.add(element)
        return new_set

    def difference(self, other_set):
        ''' difference(other_set) - return a new set that is the difference of this set and other_set '''
    
    def is_subset(self, other_set):
        ''' is_subset(other_set) - return a boolean indicating whether other_set is a subset of this set '''
