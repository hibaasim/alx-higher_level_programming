#!/usr/bin/python3
'''Module for unittesting max_integer func'''

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_int(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_order(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_float(self):
        self.assertEqual(max_integer([1, 2, 3.7, 3]), 3.7)

    def test_strings(self):
        strings = ['god', 'help', 'me']
        self.assertEqual(max_integer(strings), 'me')

if __name__ == '__main__':
    unittest.main()
