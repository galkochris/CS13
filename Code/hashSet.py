from hashtable import HashTable

class HashSet(object):
    def __init__(self, elements=None):
        self.hash = HashTable()
        if elements is not None:
            for element in elements:
                self.add(element)
    
    def size(self):
        '''size - property that tracks the number of elements in constant time'''
        return self.hash.size
    
    def contains(self, element):
        '''contains(element) - return a boolean indicating whether element is in this set'''
        return self.hash.contains(element)

    def add(self, element):
        '''add(element) - add element to this set, if not present already'''
        if self.contains(element) is False:
            self.hash.set(element, element)

    def remove(self, element):
        '''remove(element) - remove element from this set, if present, or else raise KeyError'''
        self.hash.delete(element)
    
    def union(self, other_set):
        '''union(other_set) - return a new set that is the union of this set and other_set'''
        h1 = self.hash.keys()
        h2 = other_set.hash.keys()
        return HashSet(h1 + h2)
    
    def intersection(self, other_set):
        ''' intersection(other_set) - return a new set that is the intersection of this set and other_set '''
        new_set = []
        for element in self.hash.keys():
            if other_set.contains(element):
                new_set.append(element)
        return HashSet(new_set)
    
    def difference(self, other_set):
        ''' difference(other_set) - return a new set that is the difference of this set and other_set '''
        new_set = []
        for element in self.hash.keys():
            if not other_set.contains(element):
                new_set.append(element)
        return HashSet(new_set)
    
    def is_subset(self, other_set):
        ''' is_subset(other_set) - return a boolean indicating whether other_set is a subset of this set '''
        for element in other_set.hash.keys():
            if not self.contains(element):
                return False
        return True