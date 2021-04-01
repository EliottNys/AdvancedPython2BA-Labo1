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
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
