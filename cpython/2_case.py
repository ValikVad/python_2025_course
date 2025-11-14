import unittest
import pybind11
import LowLevelStuff


class TestMult(unittest.TestCase):

    def test_with_digits(self):
        k = 14
        mass = [1, 24,36, 123, 68,13, 13, 4, 25,68]
        target = sum(mass)
        LowLevelStuff.mult(mass, k)
        self.assertEqual(sum(mass), target*k)
        
    def test_with_floats(self):
        k = 0.5
        mass = [24, 24.12, 25.75, 321, 24]
        target = sum(mass)
        LowLevelStuff.mult(mass, k)
        self.assertEqual(sum(mass), target*k)
        
    def test_with_strings1(self):
        k=9
        mass = ["AAA", "BB", "C"]
        
        expected = list(map(lambda s: s * k, mass))
       
        LowLevelStuff.mult_strings(mass, k)
       
        self.assertEqual(mass, expected)
        
    def test_with_strings2(self):
        k=11
        mass = ["AAA", "BB", "C"]
        
        expected = list(map(lambda s: s * k, mass))
       
        LowLevelStuff.mult_strings(mass, k)
       
        self.assertEqual(mass, expected)
    
        

if __name__ == '__main__':
    unittest.main()
