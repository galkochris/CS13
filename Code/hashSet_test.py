#!python

from hashSet import HashSet
import unittest

class TestSet(unittest.TestCase):
    def test_init(self):
        hs1 = HashSet([2, 2, 2])
        assert hs1.hash is not None
        assert hs1 is not None

    def test_size(self):
        hs2 = HashSet([1])
        assert hs2.size() == 1
        assert hs2.hash.size == 1
    
    def test_contains(self):
        element = 1
        hs3 = HashSet([element])
        assert hs3.contains(element) is True

    def test_add(self):
        element = 1
        hs4 = HashSet()
        hs4.add(element)
        assert hs4.contains(element) is True

    def test_remove(self):
        element = 1
        hs5 = HashSet()
        hs5.add(element)
        assert hs5.contains(element) is True
        hs5.remove(element)
        assert hs5.contains(element) is False

    def test_union(self):
        hsu = HashSet([1])
        hsun = HashSet([2])
        setunion = hsu.union(hsun)
        assert setunion.contains(1) is True

    def test_intersection(self):
        hs1 = HashSet([1])
        hs1.add(2)
        hs2 = HashSet([2])
        setinter = hs1.intersection(hs2)
        assert setinter.contains(1) is False
        assert setinter.contains(2) is True

    def test_difference(self):
        hs1 = HashSet([1])
        hs1.add(2)
        hs2 = HashSet([2])
        hs2.add(3)
        setdif = hs1.difference(hs2)
        assert setdif.contains(1) is True
        assert setdif.contains(2) is False
        assert setdif.contains(3) is False

    def test_is_subset(self):
        hs1 = HashSet([1])
        hs1.add(2)
        hs2 = HashSet([2])
        assert hs1.is_subset(hs2) is True
        
if __name__ == '__main__':
    unittest.main()