import unittest
from allocation import Building
from allocation import allocate_1, allocate_2, allocate_3, allocate_4
from allocation import allocate_1_bad, allocate_2_bad

class TestAllocations(unittest.TestCase):
    
    # Expected bad result for some of the *_bad functions - this is the goal!

    def test_less_than_10_engineering_and_art_science(self):
        self.assertEqual(allocate_1(8, 2), (Building.A, Building.B))
        self.assertEqual(allocate_1_bad(8, 2), (Building.A, Building.B))
        self.assertEqual(allocate_2(8, 2), (Building.A, Building.B))
        self.assertEqual(allocate_2_bad(8, 2), (Building.A, Building.B))
        self.assertEqual(allocate_3(8, 2), (Building.A, Building.B))
        self.assertEqual(allocate_4(8, 2), (Building.A, Building.B))
        
    def test_between_10_and_50_engineering_and_art_science(self):
        self.assertEqual(allocate_1(20, 35), (Building.B, Building.C))
        self.assertEqual(allocate_1_bad(20, 35), (Building.B, Building.C))
        self.assertEqual(allocate_2(20, 35), (Building.B, Building.C))
        self.assertEqual(allocate_2_bad(20, 35), (Building.B, Building.C))
        self.assertEqual(allocate_3(20, 35), (Building.B, Building.C))
        self.assertEqual(allocate_4(20, 35), (Building.B, Building.C))

    def test_more_than_50_engineering_and_art_science(self):
        self.assertEqual(allocate_1(60, 75), (Building.D, Building.D))
        self.assertEqual(allocate_1_bad(60, 75), (Building.D, Building.D))
        self.assertEqual(allocate_2(60, 75), (Building.D, Building.D))
        self.assertEqual(allocate_2_bad(60, 75), (Building.D, Building.D))
        self.assertEqual(allocate_3(60, 75), (Building.D, Building.D))
        self.assertEqual(allocate_4(60, 75), (Building.D, Building.D))

    def test_10_engineering_and_10_art_science(self):
        self.assertEqual(allocate_1(10, 10), (Building.B, Building.C))
        self.assertEqual(allocate_1_bad(10, 10), (Building.B, Building.C))
        self.assertEqual(allocate_2(10, 10), (Building.B, Building.C))
        self.assertEqual(allocate_2_bad(10, 10), (Building.B, Building.C))
        self.assertEqual(allocate_3(10, 10), (Building.B, Building.C))
        self.assertEqual(allocate_4(10, 10), (Building.B, Building.C))

    def test_50_engineering_and_50_art_science(self):
        self.assertEqual(allocate_1(50, 50), (Building.B, Building.C))
        self.assertEqual(allocate_1_bad(50, 50), (Building.B, Building.C))
        self.assertEqual(allocate_2(50, 50), (Building.B, Building.C))
        self.assertEqual(allocate_2_bad(50, 50), (Building.B, Building.C))
        self.assertEqual(allocate_3(50, 50), (Building.B, Building.C))
        self.assertEqual(allocate_4(50, 50), (Building.B, Building.C))
        
    def test_less_than_10_engineering_and_more_than_50_art_science(self):
        self.assertEqual(allocate_1(9, 51), (Building.A, Building.D))
        self.assertEqual(allocate_1_bad(9, 51), (Building.A, Building.D))
        self.assertEqual(allocate_2(9, 51), (Building.A, Building.D))
        self.assertEqual(allocate_2_bad(9, 51), (Building.A, Building.D))
        self.assertEqual(allocate_3(9, 51), (Building.A, Building.D))
        self.assertEqual(allocate_4(9, 51), (Building.A, Building.D))


if __name__ == '__main__':
    unittest.main()