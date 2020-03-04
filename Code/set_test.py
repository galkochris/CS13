#!python

from set import TreeSet
import unittest

class TestSet(unittest.TestCase):
    def test_init(self):
        treeset1 = TreeSet()
        assert treeset1

    def test_size(self):
        treeset2 = TreeSet(1)
        assert treeset2.size() is 1
    
    def test_contains(self):
        element = 1
        treeset3 = TreeSet(element)
        assert treeset3.contains(element) is True

    def test_add(self):
        element = 1
        treeset4 = TreeSet()
        treeset4.add(element)
        assert treeset4.contains(element) is True

    def test_remove(self):
        element = 1
        treeset5 = TreeSet()
        treeset5.add(element)
        assert treeset5.contains(element) is True
        treeset5.remove(element)
        assert treeset5.contains(element) is False

    def test_union(self):
        treesetu = TreeSet(1)
        treesetun = TreeSet(2)
        setunion = treesetu.union(treesetun)
        assert setunion.contains(1) is True
        assert setunion.contains(2) is True

    def test_intersection(self):
        treeset1 = TreeSet(1)
        treeset1.add(2)
        treeset2 = TreeSet(2)
        setinter = treeset1.intersection(treeset2)
        assert setinter.contains(1) is False
        assert setinter.contains(2) is True

    def test_difference(self):
        treeset1 = TreeSet(1)
        treeset1.add(2)
        treeset2 = TreeSet(2)
        treeset2.add(3)
        setdif = treeset1.difference(treeset2)
        assert setdif.contains(1) is True
        assert setdif.contains(2) is False
        assert setdif.contains(3) is True

    def test_is_subset(self):
        treeset1 = TreeSet(1)
        treeset1.add(2)
        treeset2 = TreeSet(2)
        assert treeset1.is_subset(treeset2) is True
        
if __name__ == '__main__':
    unittest.main()