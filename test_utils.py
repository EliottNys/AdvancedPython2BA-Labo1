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
        pass
    
    def test_roots(self):
        # À compléter...
        pass
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
