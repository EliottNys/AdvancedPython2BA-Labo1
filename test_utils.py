# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(3), 6)
        self.assertEqual(utils.fact(7), 5040)
        self.assertEqual(utils.fact(0), 1)
        self.assertEqual(utils.fact(-4), ValueError)
    
    def test_roots(self):
        self.assertEqual(utils.roots(1,-3,4), ())
        self.assertEqual(utils.roots(-4,12,-9), (3/2))
        self.assertEqual(utils.roots(2,-11,5), (5.0, 0.5))
    
    def test_integrate(self):
        self.assertEqual(utils.integrate("5",4,6), 10)
        self.assertEqual(utils.integrate("x",3,9), 36)
        self.assertEqual(utils.integrate("5*x**2+3*x-9",-3,12), 5992/2)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
