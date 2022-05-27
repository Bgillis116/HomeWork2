import unittest1


class TestSum(unittest1.TestCase):

    def test_sum(self):
        self.assertEqual(sum([2, 4, 6]), 12, "Should be 12")

    def test_sum_tuple(self):
        self.assertEqual(sum((2, 4, 6)), 12, "Should be 12")

if __name__ == '__main__':
    unittest1.main()