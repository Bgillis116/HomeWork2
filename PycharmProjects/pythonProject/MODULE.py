import unittest1


class TestSum(unittest1.TestCase):

    def test_sum(self):
        self.assertEqual(sum([2, 4, 6]), 12, "Should be 12")

    def test_sum_tuple(self):
        self.assertEqual(sum((2, 4, 6)), 12, "Should be 12")

if __name__ == '__main__':
    unittest1.main()

import unittest2

from my_sum import sum


class TestSum(unittest2.TestCase):
    def test_list_int(self):
        """"""
        Test_that_it_can_sum_a_list_of_integers
        """"""
        data = [4, 8, 12]
        result = sum(data)
        self.assertEqual(result, 24)

if _name_ == '__main__':
    unittest2.main()

import unittest1


class TestSum(unittest1.TestCase):

    def test_sum(self):
        self.assertEqual(sum([5, 10, 15]), 30, "Should be 30")

    def test_sum_tuple(self):
        self.assertEqual(sum((5, 10, 15)), 30, "Should be 30")


if __name__ == '__main__':
    unittest1.main()