import unittest
from allocation import Building
from allocation import allocate_1, allocate_2

class TestAllocations(unittest.TestCase):
    
    def test_less_than_10_engineering_and_art_science(self):
        self.assertEqual(allocate_1(8, 2), (Building.A, Building.B))
        self.assertEqual(allocate_2(8, 2), (Building.A, Building.B))
        
    def test_between_10_and_50_engineering_and_art_science(self):
        self.assertEqual(allocate_1(20, 35), (Building.B, Building.C))
        self.assertEqual(allocate_2(20, 35), (Building.B, Building.C))
        
    def test_more_than_50_engineering_and_art_science(self):
        self.assertEqual(allocate_1(60, 75), (Building.D, Building.D))
        self.assertEqual(allocate_2(60, 75), (Building.D, Building.D))
        
    def test_less_than_10_engineering_and_more_than_50_art_science(self):
        self.assertEqual(allocate_1(9, 51), (Building.A, Building.D))
        self.assertEqual(allocate_2(9, 51), (Building.A, Building.D))

if __name__ == '__main__':
    unittest.main()