"""
Module to test functions
"""


import unittest

from main import combine_dicts as function


class TestCombineDicts(unittest.TestCase):
    """ Class for test function combine_dicts """

    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}

    def test_result_1(self):
        """ Function to test data """
        self.assertEqual(function(self.dict_1, self.dict_2), {'a': 300, 'b': 200, 'c': 300},
                         "Should be {'a': 300, 'b': 200, 'c': 300}")

    def test_result_2(self):
        """ Function to test data """
        self.assertEqual(function(self.dict_1, self.dict_2, self.dict_3),
                         {'a': 600, 'b': 200, 'c': 300, 'd': 100},
                         "Should be {'a': 600, 'b': 200, 'c': 300, 'd': 100}")

    def test_result_3(self):
        """ Function to test raising ValueError"""
        a = {'a': 560.87, 'd': True}
        b = {'a': 'dd', 'd': 100}
        self.assertRaises(ValueError, function, a, b)

    def test_result_4(self):
        """ Function to test raising KeyError"""
        a = {'a': 300, 'dd': 100}
        b = {'a': 300, 'b': 100}
        self.assertRaises(KeyError, function, a, b)

    def test_result_5(self):
        """ Function to test raising KeyError"""
        a = {'a': 300, 'D': 100}
        b = {'a': 300, 'b': 100}
        self.assertRaises(KeyError, function, a, b)


if __name__ == '__main__':
    unittest.main()
