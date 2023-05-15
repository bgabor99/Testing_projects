import unittest
from allocation import allocate_1, Building

class TestAllocations(unittest.TestCase):
    
    def test_less_than_10_engineering(self):
        self.assertEqual(allocate_1(8, 25), Building.A)
        
    def test_between_10_and_50_engineering(self):
        self.assertEqual(allocate_1(20, 35), Building.B)
        
    def test_less_than_10_art_and_science(self):
        self.assertEqual(allocate_1(30, 5), Building.B)
        
    def test_between_10_and_50_art_and_science(self):
        self.assertEqual(allocate_1(45, 30), Building.B)
        
    def test_more_than_50_both_faculties(self):
        self.assertEqual(allocate_1(60, 75), Building.D)
        
    def test_default_values(self):
        self.assertEqual(allocate_1(20, 40), Building.B)
        
if __name__ == '__main__':
    unittest.main()